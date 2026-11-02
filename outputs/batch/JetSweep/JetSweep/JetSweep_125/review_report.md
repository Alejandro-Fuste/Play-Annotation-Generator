# Play-Annotation-Generator Annotation Review — JetSweep_125

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_125`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | RB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | defense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 67 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `3` | `2` | 44 | START | 44 | 98 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 68 | START | 68 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | QB | `13` | `12` | 69 | START | 69 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 69 | START | 81 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `17` | 69 | START | 69 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 69 | START | 69 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `22` | `21` | 69 | START | 69 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 69 | START | 69 | 97 |
| ✅ EXACT | `Action_SnapReceive` | RB | `9` | `8` | 80 | END | 68 | 80 |
| ✅ EXACT | `Action_Toss` | RB | `9` | `8` | 88 | START | 88 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `3` | `2` | 99 | START | 99 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | `12` | `11` | 102 | START | 102 | 153 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 166 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_LeadBlock` | 69 | 132 | 64 | inferred_complete_timeline |
| `Action_LeadBlock` | 135 | 166 | 32 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 173 | 239 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_SnapReceive` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_None` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_Toss` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_None` | 99 | 239 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_JetMotion` | 44 | 98 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 99 | 181 | 83 | inferred_complete_timeline |
| `Action_BallCarry` | 183 | 221 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 170 | 103 | inferred_complete_timeline |
| `Action_None` | 173 | 227 | 55 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 104 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 68 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 69 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 106 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 121 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 146 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 166 | 17 | inferred_complete_timeline |
| `Action_None` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 89 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_BallSnap` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 86 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 107 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 166 | 98 | inferred_complete_timeline |
| `Action_None` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 97 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 166 | 57 | inferred_complete_timeline |
| `Action_None` | 167 | 179 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 128 | 61 | inferred_complete_timeline |
| `Action_None` | 132 | 135 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 185 | 118 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 239 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 102 | 153 | 52 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 155 | 166 | 12 | inferred_complete_timeline |
| `Action_None` | 167 | 234 | 68 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 104 | 37 | inferred_complete_timeline |
| `Action_None` | 107 | 239 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 162 | 95 | inferred_complete_timeline |
| `Action_None` | 165 | 239 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 205 | 138 | inferred_complete_timeline |
| `Action_None` | 212 | 232 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 210 | 143 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 223 | 156 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 78–239 | 153 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 115–119 | 5 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 128–239 | 112 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 140–166 | 27 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 163–171 | 9 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 174–239 | 66 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 98 frames exceeds threshold 90 frames [start=69, end=166].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '12' (QB) duration 98 frames exceeds threshold 90 frames [start=69, end=166].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [68–80], lower_priority='Action_ZoneBlock' annotated_start=69, effective_Action_ZoneBlock_start=81.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 98 frames exceeds threshold 90 frames [start=69, end=166].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 98 frames exceeds threshold 90 frames [start=69, end=166].
- ⚠️ Action 'Action_None' range [68-170] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [99-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-221] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [102-153] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-234] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [69-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-239] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-107] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-232] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '21' starts at frame 69, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [69-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-146] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-220] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-239] for track '28' has 1 frames without a visible bounding box.
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