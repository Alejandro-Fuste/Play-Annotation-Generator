# Play-Annotation-Generator Annotation Review — DeepCross_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_1`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 39
- **Ball Tracks:** 6
- **Action Segments:** 88
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | QB | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `57` | `40` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | LG | `18` | `18` | 6 | START | 6 | 8 |
| ✅ EXACT | `Action_PassBlock` | RT | `14` | `14` | 9 | START | 9 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 9 | START | 9 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 9 | START | 9 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 9 | START | 9 | 21 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `21` | 9 | START | 9 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | QB | `11` | `11` | 20 | START | 20 | 116 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `11` | `11` | 20 | END | N/A | N/A |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 117 | START | 117 | 124 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `57` | `40` | 198 | START | 198 | 269 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 20 | 116 | 97 | inferred_complete_timeline |
| `Action_ThrowPass` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 125 | 152 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 187 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 117 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 50 | 45 | inferred_complete_timeline |
| `Action_None` | 53 | 142 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 196 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 31 | 26 | inferred_complete_timeline |
| `Action_None` | 33 | 168 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 147 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 8 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 121 | 113 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 171 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 136 | 128 | inferred_complete_timeline |
| `Action_PassBlock` | 138 | 150 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 100 | 75 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 166 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 163 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 25 | 20 | inferred_complete_timeline |
| `Action_None` | 28 | 155 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 131 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 109 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 35 | 30 | inferred_complete_timeline |
| `Action_None` | 37 | 142 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 269 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 91 | 86 | inferred_complete_timeline |
| `Action_None` | 100 | 138 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 166 | 161 | inferred_complete_timeline |
| `Action_None` | 168 | 202 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 120 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 136 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 109 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–202 | 201 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 35–69 | 35 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 51–172 | 99 | 3 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 84–175 | 84 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 95–97 | 3 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 106–167 | 61 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 135–269 | 117 | 3 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 135–201 | 63 | 3 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 137–146 | 10 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 143–163 | 21 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 143–201 | 59 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 147–269 | 123 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 148–269 | 122 | 2 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 149–157 | 9 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 183–190 | 5 | 2 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 239–269 | 31 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | 0 | 6 | 7 | 100.0% | None |
| `23` | `26` | 34 | 57 | 24 | 100.0% | None |
| `30` | `42` | 117 | 121 | 5 | 100.0% | None |
| `31` | `45` | 129 | 157 | 19 | 65.5% | 132–133, 136–137, 140–145 |
| `32` | `46` | 133 | 149 | 8 | 47.1% | 134–135, 138–142, 146–147 |
| `36` | `50` | 141 | 141 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `11` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `11` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Overlapping action conflict at frame 20 for track '11': 'Action_SnapReceive' vs 'Action_RunDeepCrossRoute'. Overriding with 'Action_RunDeepCrossRoute'.
- ⚠️ Action 'Action_None' range [6-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-25] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-202] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [125-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [138-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-31] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-168] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-100] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-166] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-69] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-172] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-91] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-119] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-167] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-192] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-163] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-201] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-269] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-269] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>