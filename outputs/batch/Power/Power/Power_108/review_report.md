# Play-Annotation-Generator Annotation Review — Power_108

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_108`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | QB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 12 | START | 12 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 12 | START | 12 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 12 | START | 12 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 12 | START | 12 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 12 | START | 12 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 12 | START | 12 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 12 | START | 12 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `2` | `2` | 96 | START | 96 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `9` | 96 | START | 96 | 101 |
| ✅ EXACT | `Action_PullBlock` | QB | `6` | `6` | 96 | START | 96 | 129 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–294
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 95 | 84 | inferred_complete_timeline |
| `Action_PullBlock` | 96 | 129 | 34 | inferred_complete_timeline |
| `Action_None` | 130 | 294 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–219
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 219 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–253
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 201 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 253 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 12–277
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 158 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 178 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 277 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–230
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 95 | 84 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 101 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_None` | 152 | 164 | 13 | inferred_complete_timeline |
| `Action_None` | 167 | 174 | 8 | inferred_complete_timeline |
| `Action_None` | 199 | 230 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–244
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 114 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 141 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 149 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 164 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 244 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–294
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 95 | 84 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 114 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 122 | 129 | 8 | inferred_complete_timeline |
| `Action_None` | 130 | 130 | 1 | inferred_complete_timeline |
| `Action_None` | 134 | 152 | 19 | inferred_complete_timeline |
| `Action_None` | 165 | 294 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 187 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 299 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–151
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 151 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 20 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 31 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 85 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 115 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 165 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 186 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 299 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–100
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 93 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 178 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 299 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–135
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 135 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 247 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 287 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 122–217 | 96 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 147–218 | 72 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 153–299 | 147 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 173–195 | 23 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 190–248 | 59 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 191–298 | 38 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 196–299 | 96 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 214–299 | 86 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 228–288 | 61 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 242–299 | 50 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 55 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [12-219] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-119] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [122-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 130, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [130-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-294] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-135] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-201] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-294] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-164] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-244] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-164] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-230] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-187] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-277] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-20] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-31] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-85] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-218] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-248] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-226] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-277] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-295] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-288] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>