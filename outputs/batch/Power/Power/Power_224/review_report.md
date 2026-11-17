# Play-Annotation-Generator Annotation Review — Power_224

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_224`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 122
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_PullBlock` | DT1 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 4 | START | 4 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 4 | START | 4 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 4 | START | 20 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 4 | START | 4 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 4 | START | 4 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 4 | START | 4 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 4 | START | 4 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 4 | START | 4 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `14` | 126 | START | 126 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `4` | `4` | 126 | START | 126 | 154 |
| ⚠️ START CHANGED | `Action_PullBlock` | DT1 | `10` | `10` | 126 | START | 130 | 131 |

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
- **Visible Frames:** 4–224
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 224 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 210 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–292
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 162 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 171 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 263 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 292 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 4–159
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 159 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 34 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 129 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 168 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 299 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 20–178
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 125 | 106 | inferred_complete_timeline |
| `Action_DownBlock` | 126 | 131 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 145 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 178 | 178 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 146 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 178 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 193 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–275
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 125 | 122 | inferred_complete_timeline |
| `Action_DownBlock` | 126 | 154 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 165 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 168 | 177 | 10 | inferred_complete_timeline |
| `Action_None` | 178 | 200 | 23 | inferred_complete_timeline |
| `Action_None` | 203 | 241 | 39 | inferred_complete_timeline |
| `Action_None` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 4–284
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 114 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 126 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 158 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 284 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–131
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 123 | 120 | inferred_complete_timeline |
| `Action_PullBlock` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 23 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 30 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 64 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 122 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 195 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 4–234
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 189 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 234 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 28 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 66 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 123 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 196 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 272 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 299 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–205
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 191 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 205 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 4–173 | 103 | 6 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 151–154 | 4 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 166–229 | 38 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 179–299 | 121 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 179–299 | 118 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 198–294 | 97 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 199–275 | 77 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 211–219 | 9 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 223–227 | 5 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 229–271 | 40 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 252–295 | 27 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 258–299 | 42 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 263–276 | 14 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 283–285 | 3 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 285–299 | 12 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (3 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `10` (DT1): Annotated start 126 != Inferred start 130

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 450: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [4-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-114] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-173] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-241] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-171] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-263] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-292] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-28] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-33] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-66] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [130-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-8] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-30] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-64] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-34] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-145] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 178, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [178-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-201] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-299] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-294] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-227] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-277] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>