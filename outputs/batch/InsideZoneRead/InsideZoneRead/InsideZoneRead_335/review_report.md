# Play-Annotation-Generator Annotation Review — InsideZoneRead_335

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_335`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT2 | defense | `1` | `0` |
| ✅ EXACT | `Action_Keep` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 2 | START | 2 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 2 | START | 2 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 2 | START | 2 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 2 | START | 2 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 2 | START | 2 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 2 | START | 2 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 2 | START | 2 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 2 | START | 2 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 2 | START | 2 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 2 | START | 2 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 2 | START | 2 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 29 | START | 29 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `16` | 32 | START | 32 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `17` | 32 | START | 32 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 32 | START | 41 | 47 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 32 | START | 32 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `2` | 32 | START | 32 | 110 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 40 | END | 29 | 40 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `4` | 47 | START | 47 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT2 | `1` | `0` | 48 | START | 48 | 59 |
| ✅ EXACT | `Action_Keep` | QB | `5` | `4` | 62 | START | 62 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 76 | START | 76 | 143 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 110 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–146
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 40 | 12 | inferred_complete_timeline |
| `Action_None` | 41 | 46 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_Keep` | 62 | 75 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 143 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 145 | 146 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 2–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 138 | 110 | inferred_complete_timeline |
| `Action_None` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_None` | 169 | 180 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 2–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 2–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 2–163
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 163 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 2–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 2–173
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 31 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 110 | 79 | inferred_complete_timeline |
| `Action_None` | 111 | 147 | 37 | inferred_complete_timeline |
| `Action_None` | 149 | 173 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 2–162
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 31 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 110 | 79 | inferred_complete_timeline |
| `Action_None` | 111 | 162 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 2–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 40 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 110 | 48 | inferred_complete_timeline |
| `Action_None` | 111 | 162 | 52 | inferred_complete_timeline |
| `Action_None` | 164 | 180 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 2–62
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 31 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 62 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–172
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 31 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 110 | 79 | inferred_complete_timeline |
| `Action_None` | 111 | 172 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 2–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 64 | 36 | inferred_complete_timeline |
| `Action_None` | 67 | 180 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–96
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 48 | 20 | inferred_complete_timeline |
| `Action_None` | 50 | 70 | 21 | inferred_complete_timeline |
| `Action_None` | 72 | 77 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 2–90
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 47 | 46 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 48 | 59 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 85 | 90 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 78 | 50 | inferred_complete_timeline |
| `Action_None` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_None` | 88 | 105 | 18 | inferred_complete_timeline |
| `Action_None` | 113 | 180 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 2–77
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 77 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–169
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 108 | 80 | inferred_complete_timeline |
| `Action_None` | 114 | 169 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 2–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 2–162
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 162 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–167
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 167 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 2–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 51–180 | 130 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 78–180 | 103 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 90–177 | 84 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 116–176 | 61 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `1` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [29–40], lower_priority='Action_ZoneBlock' annotated_start=32, effective_Action_ZoneBlock_start=41.
- ⚠️ Action 'Action_BlockSecondLevel' range [48-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [61-64] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [76-78] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [80-82] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [85-90] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-167] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [145-146] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-70] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-162] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-162] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-168] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>