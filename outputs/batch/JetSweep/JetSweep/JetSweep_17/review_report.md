# Play-Annotation-Generator Annotation Review — JetSweep_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_17`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 29
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `9` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_JetMotion` | WR | `3` | `2` | 2 | START | 2 | 64 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 37 | START | 37 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `16` | `15` | 40 | START | 40 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `14` | 40 | START | 40 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 40 | START | 52 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 40 | START | 40 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 40 | START | 40 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 40 | START | 40 | 111 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 51 | END | 37 | 51 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 57 | START | 57 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `3` | `2` | 65 | START | 65 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `20` | `19` | 69 | START | 69 | 106 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `15` | `14` | 111 | BOUNDARY | 77 | 111 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `20` | `19` | 111 | BOUNDARY | 111 | 111 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `22` | `21` | 111 | BOUNDARY | 75 | 111 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `22` | `21` | 111 | BOUNDARY | 75 | 111 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `9` | `8` | 111 | BOUNDARY | 40 | 111 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 51 | 15 | inferred_complete_timeline |
| `Action_None` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_Toss` | 57 | 64 | 8 | inferred_complete_timeline |
| `Action_None` | 65 | 210 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 102 | 66 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 2 | 64 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 65 | 165 | 101 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 188 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 193 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 197 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 180 | 144 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_LeadBlock` | 40 | 78 | 39 | inferred_complete_timeline |
| `Action_LeadBlock` | 80 | 111 | 32 | inferred_complete_timeline |
| `Action_None` | 112 | 203 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 111 | 72 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 74 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 111 | 35 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 71 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 111 | 37 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 51 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 68 | 17 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 69 | 106 | 38 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 111 | 111 | 1 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 71 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 125 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 74 | 38 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 173 | 137 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 183 | 210 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 116 | 80 | inferred_complete_timeline |
| `Action_None` | 118 | 210 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 176 | 140 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 162 | 126 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 45–53 | 9 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 83–84 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 124–210 | 86 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 125–210 | 84 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 148–165 | 10 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 195–203 | 6 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 206–208 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [37–51], lower_priority='Action_ZoneBlock' annotated_start=40, effective_Action_ZoneBlock_start=52.
- ⚠️ Action 'Action_None' range [37-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [65-165] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-188] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [195-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-176] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-173] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-162] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-74] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [40-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [69-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-71] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-53] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-198] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '29' has 1 frames without a visible bounding box.
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