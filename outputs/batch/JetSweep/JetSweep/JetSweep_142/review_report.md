# Play-Annotation-Generator Annotation Review — JetSweep_142

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_142`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | RB | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `16` | `15` | 6 | START | 6 | 55 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 23 | START | 23 | 40 |
| ✅ EXACT | `Action_LeadBlock` | TE | `10` | `9` | 25 | START | 25 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | RB | `15` | `14` | 25 | START | 25 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `11` | 25 | START | 25 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 25 | START | 41 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 25 | START | 25 | 52 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 25 | START | 25 | 83 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `7` | 25 | START | 25 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 40 | END | 23 | 40 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 45 | START | 45 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `15` | 56 | START | 56 | 197 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 88 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 40 | 18 | inferred_complete_timeline |
| `Action_None` | 41 | 44 | 4 | inferred_complete_timeline |
| `Action_Toss` | 45 | 55 | 11 | inferred_complete_timeline |
| `Action_None` | 56 | 86 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SealBlock` | 25 | 86 | 62 | inferred_complete_timeline |
| `Action_SealBlock` | 89 | 133 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_LeadBlock` | 25 | 88 | 64 | inferred_complete_timeline |
| `Action_None` | 89 | 145 | 57 | inferred_complete_timeline |
| `Action_None` | 147 | 210 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 83 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 88 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 40 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 73 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 86 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 88 | 64 | inferred_complete_timeline |
| `Action_None` | 89 | 103 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 52 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 88 | 35 | inferred_complete_timeline |
| `Action_None` | 89 | 96 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 82 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 205 | 183 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 90 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 54 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 96 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 110 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 179 | 157 | inferred_complete_timeline |
| `Action_None` | 188 | 194 | 7 | inferred_complete_timeline |
| `Action_None` | 196 | 203 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 6–210 | 202 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 60–94 | 35 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 73–148 | 75 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 111–210 | 100 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 112–121 | 7 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 117–210 | 94 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 146–181 | 36 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 150–200 | 51 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 182–210 | 26 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 186–210 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SealBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [23–40], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=41.
- ⚠️ Action 'Action_None' range [23-96] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-52] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-83] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-82] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-145] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 56, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [56-86] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-73] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [25-86] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [89-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-197] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [201-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-117] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-181] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '26' has 1 frames without a visible bounding box.
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

</details>