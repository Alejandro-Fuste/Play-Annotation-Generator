# Play-Annotation-Generator Annotation Review — JetSweep_135

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_135`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | CB2 | defense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR2 | `16` | `15` | 0 | START | 0 | 40 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | CB2 | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 10 | START | 10 | 22 |
| ✅ EXACT | `Action_LeadBlock` | RB | `19` | `18` | 11 | START | 11 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `14` | 11 | START | 11 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 11 | START | 11 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `20` | 11 | START | 11 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 11 | START | 11 | 32 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `9` | `8` | 11 | START | 23 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 22 | END | 10 | 22 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 25 | START | 25 | 40 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `16` | `15` | 41 | START | 41 | 210 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `7` | `6` | 50 | START | 50 | 98 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 98 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 22 | 13 | inferred_complete_timeline |
| `Action_None` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_Toss` | 25 | 40 | 16 | inferred_complete_timeline |
| `Action_None` | 41 | 127 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_LeadBlock` | 11 | 98 | 88 | inferred_complete_timeline |
| `Action_None` | 99 | 189 | 91 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 41 | 210 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 117 | 108 | inferred_complete_timeline |
| `Action_None` | 120 | 127 | 8 | inferred_complete_timeline |
| `Action_None` | 129 | 160 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 115 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 210 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 98 | 88 | inferred_complete_timeline |
| `Action_None` | 99 | 133 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 98 | 88 | inferred_complete_timeline |
| `Action_None` | 99 | 194 | 96 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 22 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 98 | 76 | inferred_complete_timeline |
| `Action_None` | 99 | 167 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 18 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 32 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 49 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 50 | 98 | 49 | inferred_complete_timeline |
| `Action_None` | 99 | 167 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 96 | 87 | inferred_complete_timeline |
| `Action_None` | 100 | 135 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 41 | 32 | inferred_complete_timeline |
| `Action_None` | 43 | 49 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 157 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 122 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 164 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 29–30 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 31–210 | 180 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 53–63 | 11 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 72–91 | 11 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 74–188 | 115 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 134–139 | 6 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 138–158 | 17 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 156–158 | 3 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `9` (C): Annotated start 11 != Inferred start 23

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [10–22], lower_priority='Action_ZoneBlock' annotated_start=11, effective_Action_ZoneBlock_start=23.
- ⚠️ Action 'Action_None' range [10-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-127] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-32] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-167] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-164] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [41-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-194] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-63] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-91] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '32' has 1 frames without a visible bounding box.
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