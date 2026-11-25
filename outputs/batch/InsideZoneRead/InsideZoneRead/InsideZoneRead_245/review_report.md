# Play-Annotation-Generator Annotation Review — InsideZoneRead_245

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_245`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `4` | `3` |
| ✅ EXACT | `Action_ReadDefender` | DE1 | defense | `4` | `3` |
| ✅ EXACT | `Action_Keep` | DE1 | defense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE1 | defense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_BallSnap` | QB | `12` | `11` | 0 | START | 0 | 4 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `1` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `11` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `12` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `14` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `5` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `9` | `Group` | 0 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `10` | 0 | START | 0 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `14` | 0 | START | 0 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 0 | START | 0 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 0 | START | 0 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 0 | START | 0 | 71 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `4` | `3` | 4 | END | 0 | 4 |
| ✅ EXACT | `Action_ReadDefender` | DE1 | `4` | `3` | 10 | START | 10 | 28 |
| ✅ EXACT | `Action_Keep` | DE1 | `4` | `3` | 29 | START | 29 | 36 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE1 | `4` | `3` | 45 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 75 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_BallSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 157 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 88 | 102 | 15 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 169 | 11 | inferred_complete_timeline |
| `Action_None` | 172 | 180 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 75 | 1 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 102 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_None` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_None` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_None` | 107 | 180 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 138 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 75 | 32 | inferred_complete_timeline |
| `Action_None` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_None` | 89 | 102 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_SnapReceive` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 9 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 10 | 28 | 19 | inferred_complete_timeline |
| `Action_Keep` | 29 | 36 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 44 | 76 | 33 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 110 | 19 | inferred_complete_timeline |
| `Action_None` | 112 | 180 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 54 | 180 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 79 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 87 | 180 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 180 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 146 | 159 | 14 | inferred_complete_timeline |
| `Action_None` | 162 | 180 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–134 | 106 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 46–70 | 23 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 91–180 | 90 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 96–180 | 83 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 118–180 | 46 | 4 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 132–180 | 39 | 5 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 160–179 | 17 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 162–180 | 19 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (DE1)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 490: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '3' has invalid range: start=45, end=36. Clamping end to start.
- ⚠️ Action 'Action_None' range [0-153] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-136] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-159] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [29-36] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-122] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-64] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-180] for track '6' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-81] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [0-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-157] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [0-62] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [0-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-102] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [0-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-169] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [0-71] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-116] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-166] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-155] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-140] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_245'; source metadata written as null.

</details>