# Play-Annotation-Generator Annotation Review — JetSweep_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_9`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 64
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 29
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_Toss` | QB | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `16` | `15` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `10` | `9` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `19` | `18` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `21` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR | `16` | `15` | 0 | START | 0 | 43 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 24 | START | 24 | 33 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 25 | START | 25 | 74 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 25 | START | 25 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 25 | START | 25 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 25 | START | 25 | 74 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `21` | `20` | 25 | START | 34 | 64 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 33 | END | 24 | 33 |
| ✅ EXACT | `Action_Toss` | QB | `22` | `21` | 36 | START | 36 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `16` | `15` | 44 | START | 44 | 163 |
| ✅ EXACT | `Action_LeadBlock` | RB | `14` | `13` | 44 | START | 44 | 74 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `15` | `14` | 49 | START | 49 | 74 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `10` | `9` | 74 | BOUNDARY | 25 | 74 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `15` | `14` | 74 | BOUNDARY | 49 | 74 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `19` | `18` | 74 | BOUNDARY | 25 | 74 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `20` | `19` | 74 | BOUNDARY | 25 | 74 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `21` | `20` | 74 | BOUNDARY | N/A | 74 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 33 | 10 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_Toss` | 36 | 43 | 8 | inferred_complete_timeline |
| `Action_None` | 44 | 157 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_LeadBlock` | 44 | 74 | 31 | inferred_complete_timeline |
| `Action_None` | 75 | 180 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 170 | 147 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 44 | 163 | 120 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 180 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 146 | 123 | inferred_complete_timeline |
| `Action_None` | 156 | 168 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 48 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 49 | 74 | 26 | inferred_complete_timeline |
| `Action_None` | 75 | 180 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 74 | 50 | inferred_complete_timeline |
| `Action_None` | 75 | 180 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 33 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 64 | 31 | inferred_complete_timeline |
| `Action_None` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 113 | 15 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 173 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 74 | 50 | inferred_complete_timeline |
| `Action_None` | 75 | 95 | 21 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 74 | 50 | inferred_complete_timeline |
| `Action_None` | 75 | 123 | 49 | inferred_complete_timeline |
| `Action_None` | 126 | 171 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 93 | 70 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 180 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 47 | 24 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 166 | 143 | inferred_complete_timeline |
| `Action_None` | 169 | 180 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 108 | 85 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 118 | 129 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 157 | 134 | inferred_complete_timeline |
| `Action_None` | 163 | 170 | 8 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 46–48 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 82–180 | 97 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 83–114 | 29 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 131–134 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 136–167 | 32 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 141–180 | 40 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `21` (C): Annotated start 25 != Inferred start 34
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [24–33], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=34.
- ⚠️ Action 'Action_None' range [24-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-170] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-129] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-95] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [44-163] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-169] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-146] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-171] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '27' has 2 frames without a visible bounding box.
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

</details>