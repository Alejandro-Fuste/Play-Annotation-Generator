# Play-Annotation-Generator Annotation Review — CrackToss_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_76`
- **Frame Range:** 0 to 249 (250 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 249
- **Player Tracks:** 36
- **Ball Tracks:** 1
- **Action Segments:** 84
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_CrackBlock` | DE1 | defense | `11` | `10` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_PullBlock` | DT1 | defense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_Toss` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 8 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 8 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 8 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 8 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 8 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 8 | START | 0 | 109 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 110 | START | 110 | 117 |
| ✅ EXACT | `Action_CrackBlock` | DE1 | `11` | `10` | 113 | START | 113 | 176 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `17` | `16` | 113 | START | 113 | 176 |
| ✅ EXACT | `Action_PullBlock` | DT1 | `2` | `1` | 113 | START | 113 | 176 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `21` | `20` | 117 | END | 110 | 117 |
| ✅ EXACT | `Action_Toss` | Position_Unknown | `21` | `20` | 124 | START | 124 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `22` | `21` | 140 | START | 140 | 232 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 176 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 132 | 23 | inferred_complete_timeline |
| `Action_None` | 135 | 249 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_BallSnap` | 110 | 117 | 8 | inferred_complete_timeline |
| `Action_None` | 118 | 130 | 13 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_CrackBlock` | 113 | 176 | 64 | inferred_complete_timeline |
| `Action_None` | 177 | 249 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 169 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PullBlock` | 113 | 176 | 64 | inferred_complete_timeline |
| `Action_None` | 177 | 230 | 54 | inferred_complete_timeline |
| `Action_None` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 247 | 13 | inferred_complete_timeline |
| `Action_None` | 249 | 249 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 249 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 170 | 61 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 249 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 241 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 8–242 | 235 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 8–249 | 242 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 8–190 | 183 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 8–249 | 242 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 8–225 | 218 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 8–174 | 167 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 8–238 | 227 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 8–204 | 194 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 59–62 | 4 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 69–173 | 71 | 8 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 128–249 | 122 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 136–249 | 109 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 147–249 | 99 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 183–249 | 67 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 189–249 | 57 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 215–244 | 20 | 3 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 223–228 | 6 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 234–236 | 3 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 236–249 | 14 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 242–245 | 4 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 244–249 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | 0 | 0 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 154: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-247] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-242] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-190] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-225] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [237-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-204] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-71] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-87] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-101] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-173] for track '24' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-185] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-235] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-160] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-244] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '36' has 1 frames without a visible bounding box.
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

</details>