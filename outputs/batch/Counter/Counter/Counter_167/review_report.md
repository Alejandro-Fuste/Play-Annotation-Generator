# Play-Annotation-Generator Annotation Review — Counter_167

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_167`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | DT1 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | WR | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 149 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `14` | `13` | 150 | START | 150 | 153 |
| ✅ EXACT | `Action_DownBlock` | DT1 | `14` | `13` | 154 | START | 154 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `17` | `16` | 154 | START | 154 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `18` | `17` | 154 | START | 154 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `22` | `21` | 154 | START | 154 | 187 |
| ✅ EXACT | `Action_PullLeadBlock` | WR | `8` | `7` | 154 | START | 154 | 186 |
| ✅ EXACT | `Action_SnapReceive` | RG | `13` | `12` | 163 | END | 150 | 163 |
| ✅ EXACT | `Action_Handoff` | RG | `13` | `12` | 174 | START | 174 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `20` | 196 | START | 196 | 211 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 231 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 212 | 63 | inferred_complete_timeline |
| `Action_None` | 238 | 255 | 18 | inferred_complete_timeline |
| `Action_None` | 262 | 281 | 20 | inferred_complete_timeline |
| `Action_None` | 284 | 321 | 38 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 255 | 19 | inferred_complete_timeline |
| `Action_None` | 259 | 329 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 154 | 186 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 174 | 25 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_None` | 190 | 199 | 10 | inferred_complete_timeline |
| `Action_None` | 202 | 213 | 12 | inferred_complete_timeline |
| `Action_None` | 216 | 224 | 9 | inferred_complete_timeline |
| `Action_None` | 227 | 301 | 75 | inferred_complete_timeline |
| `Action_None` | 306 | 320 | 15 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_SnapReceive` | 150 | 163 | 14 | inferred_complete_timeline |
| `Action_None` | 164 | 173 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 195 | 22 | inferred_complete_timeline |
| `Action_None` | 196 | 329 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_BallSnap` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 231 | 78 | inferred_complete_timeline |
| `Action_None` | 232 | 301 | 70 | inferred_complete_timeline |
| `Action_None` | 303 | 317 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 206 | 57 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 290 | 141 | inferred_complete_timeline |
| `Action_None` | 292 | 296 | 5 | inferred_complete_timeline |
| `Action_None` | 298 | 329 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–199 | 170 | 7 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–253 | 243 | 7 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–329 | 269 | 9 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–178 | 165 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–329 | 283 | 10 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–294 | 247 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–303 | 259 | 15 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 3–215 | 123 | 6 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 51–52 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 228–329 | 102 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 238–329 | 92 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 239–240 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 239–329 | 91 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 242–255 | 14 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 259–329 | 71 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 272–329 | 58 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 276–329 | 53 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 313–329 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 336: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [150-290] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [154-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-199] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-301] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-320] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-255] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-329] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-212] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-255] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-321] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-301] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-317] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-78] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-188] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-222] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-253] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [164-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-261] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-285] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-178] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-50] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-205] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-249] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-329] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-211] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-247] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-289] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-20] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-43] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-179] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [234-303] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-153] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [154-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [198-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [202-215] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-255] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-329] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '31' has 2 frames without a visible bounding box.
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

</details>