# Play-Annotation-Generator Annotation Review — JetSweep_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_98`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | WR3 | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 69 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `1` | `0` | 29 | START | 29 | 93 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 69 | START | 69 | 80 |
| ✅ EXACT | `Action_LeadBlock` | WR3 | `6` | `5` | 70 | START | 70 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `17` | 70 | START | 70 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 70 | START | 70 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 70 | START | 70 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 70 | START | 81 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 70 | START | 70 | 144 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 80 | END | 69 | 80 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 88 | START | 88 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `1` | `0` | 94 | START | 94 | 200 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_SnapReceive` | 69 | 80 | 12 | inferred_complete_timeline |
| `Action_None` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_Toss` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 210 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_JetMotion` | 29 | 93 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 200 | 107 | inferred_complete_timeline |
| `Action_BallCarry` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_LeadBlock` | 70 | 144 | 75 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 95 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 144 | 41 | inferred_complete_timeline |
| `Action_None` | 145 | 170 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 144 | 75 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_BallSnap` | 69 | 80 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 105 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 144 | 37 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 144 | 75 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 144 | 75 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 150 | 82 | inferred_complete_timeline |
| `Action_None` | 155 | 210 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 108 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 190 | 122 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 140 | 72 | inferred_complete_timeline |
| `Action_None` | 147 | 210 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 180 | 112 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 206 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 69–75 | 7 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 117–160 | 44 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 158–210 | 53 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 198: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [69–80], lower_priority='Action_ZoneBlock' annotated_start=70, effective_Action_ZoneBlock_start=81.
- ⚠️ Action 'Action_BallCarry' range [94-200] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-190] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-95] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-75] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '29' has 1 frames without a visible bounding box.
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

</details>