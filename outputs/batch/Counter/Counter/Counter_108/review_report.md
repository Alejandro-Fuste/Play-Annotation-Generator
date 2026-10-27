# Play-Annotation-Generator Annotation Review — Counter_108

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_108`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT2 | defense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 116 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `16` | `15` | 111 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | RT | `1` | `0` | 117 | START | 117 | 241 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `16` | `15` | 117 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `9` | `8` | 117 | START | 117 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `3` | `2` | 117 | START | 117 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT2 | `5` | `4` | 117 | START | 117 | 157 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 127 | END | 111 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `13` | `12` | 151 | START | 151 | 195 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 241 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_SnapReceive` | 111 | 127 | 17 | inferred_complete_timeline |
| `Action_None` | 128 | 150 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 195 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 255 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 258 | 326 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 143 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 164 | 54 | inferred_complete_timeline |
| `Action_None` | 167 | 194 | 28 | inferred_complete_timeline |
| `Action_None` | 200 | 329 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PullBlock` | 117 | 139 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 143 | 180 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 186 | 241 | 56 | inferred_complete_timeline |
| `Action_None` | 242 | 325 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 190 | 74 | inferred_complete_timeline |
| `Action_DownBlock` | 194 | 241 | 48 | inferred_complete_timeline |
| `Action_None` | 242 | 324 | 83 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 241 | 125 | inferred_complete_timeline |
| `Action_None` | 242 | 318 | 77 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 216 | 106 | inferred_complete_timeline |
| `Action_None` | 220 | 329 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 328 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 117 | 157 | 41 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 184 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 186 | 76 | inferred_complete_timeline |
| `Action_None` | 198 | 329 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 193 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 157 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 110 | 70 | inferred_complete_timeline |
| `Action_None` | 111 | 329 | 219 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–203 | 199 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 121–327 | 197 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 152–182 | 31 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 160–329 | 167 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 162–324 | 163 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 199–222 | 24 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 207–212 | 6 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 211–329 | 110 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 213–261 | 49 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 243–317 | 66 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 245–329 | 82 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 252–314 | 58 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 265–280 | 16 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 273–329 | 57 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 276–329 | 54 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 294–303 | 5 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 301–318 | 5 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 302–329 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `16` (C)
- ❌ Missing segment for action `Action_DownBlock` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 218: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 218: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '0' (RT) duration 125 frames exceeds threshold 90 frames [start=117, end=241].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (LG) duration 125 frames exceeds threshold 90 frames [start=117, end=241].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 125 frames exceeds threshold 90 frames [start=117, end=241].
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=111, end=19. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '15' has invalid range: start=117, end=19. Clamping end to start.
- ⚠️ Action 'Action_None' range [242-318] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-164] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [117-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [143-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [182-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-325] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [117-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [162-163] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-328] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-324] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-157] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-255] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-326] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-216] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-203] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-148] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-327] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-324] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-314] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-261] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-298] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-317] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-291] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-308] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-280] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>