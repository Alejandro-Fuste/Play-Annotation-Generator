# Play-Annotation-Generator Annotation Review — Power_106

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_106`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 24 | START | 24 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 24 | START | 24 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 24 | START | 27 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 24 | START | 42 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 24 | START | 24 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 24 | START | 24 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 24 | START | 24 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 24 | START | 24 | 167 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `12` | `12` | 150 | START | 161 | 162 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | `4` | `4` | 150 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `4` | `4` | 150 | START | 150 | 162 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 24–178
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 167 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 178 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 24–248
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 102 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 122 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 157 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 180 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 192 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 216 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 248 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 24–329
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 158 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 224 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 329 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 42–153
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 55 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 75 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 102 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 110 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 153 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 24–189
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 189 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–162
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 96 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 148 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 24–176
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 149 | 126 | inferred_complete_timeline |
| `Action_PullBlock` | 150 | 162 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 169 | 176 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 27–196
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 154 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 196 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 329 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 24–265
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 240 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 257 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 265 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 29–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 329 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 176 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 329 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 226 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 275 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 329 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 24–130
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 130 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 24–265 | 242 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 24–329 | 291 | 8 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 162–174 | 13 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 165–329 | 164 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 175–329 | 155 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 180–205 | 26 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 181–329 | 140 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 189–225 | 35 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 191–329 | 130 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 194–328 | 133 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 202–329 | 126 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 213–329 | 117 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 222–225 | 4 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 228–329 | 85 | 6 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 242–247 | 6 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 247–329 | 81 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 255–329 | 75 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 271–329 | 59 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 274–329 | 50 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 278–280 | 3 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 296–327 | 32 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 296–308 | 7 | 2 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 301–329 | 29 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 312–329 | 18 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 319–329 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `12` (C): Annotated start 150 != Inferred start 161
- ❌ Missing segment for action `Action_DownBlock` on target `4` (RG)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Overlapping action conflict at frame 150 for track '4': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
- ⚠️ Action 'Action_PreSnap' range [24-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-176] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-257] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-265] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [150-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [169-176] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-226] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-275] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-122] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-180] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-248] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-167] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-237] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-243] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-252] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-274] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-189] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-154] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-196] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-329] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-75] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-102] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-110] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-221] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-256] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-265] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-277] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-324] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-231] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-239] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-232] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-243] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-280] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-286] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-253] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-329] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-289] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-329] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-280] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-327] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>