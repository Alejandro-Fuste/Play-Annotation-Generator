# Play-Annotation-Generator Annotation Review — InsideZoneRead_295

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_295`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB4 | defense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_Keep` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | RT | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | CB4 | `13` | `12` | 19 | START | 19 | 30 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `10` | `9` | 22 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 22 | START | 22 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 22 | START | 22 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 22 | START | 22 | 51 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `20` | 22 | START | 22 | 106 |
| ✅ EXACT | `Action_SnapReceive` | RT | `10` | `9` | 30 | END | 19 | 30 |
| ✅ EXACT | `Action_ReadDefender` | RT | `10` | `9` | 35 | START | 35 | 47 |
| ✅ EXACT | `Action_Keep` | RT | `10` | `9` | 48 | START | 48 | 67 |
| ✅ EXACT | `Action_BallCarry` | RT | `10` | `9` | 68 | START | 68 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 106 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 163 | 145 | inferred_complete_timeline |
| `Action_None` | 166 | 177 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_None` | 54 | 89 | 36 | inferred_complete_timeline |
| `Action_None` | 101 | 109 | 9 | inferred_complete_timeline |
| `Action_None` | 119 | 126 | 8 | inferred_complete_timeline |
| `Action_None` | 137 | 180 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 166 | 148 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 121 | 103 | inferred_complete_timeline |
| `Action_None` | 140 | 180 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 106 | 85 | inferred_complete_timeline |
| `Action_None` | 107 | 176 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 106 | 85 | inferred_complete_timeline |
| `Action_None` | 107 | 180 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 38 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 106 | 53 | inferred_complete_timeline |
| `Action_None` | 107 | 180 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 51 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 106 | 45 | inferred_complete_timeline |
| `Action_None` | 107 | 180 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_None` | 31 | 34 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 35 | 47 | 13 | inferred_complete_timeline |
| `Action_Keep` | 48 | 67 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 180 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 72 | 54 | inferred_complete_timeline |
| `Action_None` | 80 | 120 | 41 | inferred_complete_timeline |
| `Action_None` | 122 | 160 | 39 | inferred_complete_timeline |
| `Action_None` | 165 | 174 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 121 | 103 | inferred_complete_timeline |
| `Action_None` | 125 | 169 | 45 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 168 | 150 | inferred_complete_timeline |
| `Action_None` | 174 | 180 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 137 | 119 | inferred_complete_timeline |
| `Action_None` | 140 | 180 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 156 | 138 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_None` | 31 | 180 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 103–107 | 5 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 140–164 | 18 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `10` (RT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ 2 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 2 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 4 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '9' has invalid range: start=22, end=18. Clamping end to start.
- ⚠️ Action 'Action_None' range [19-121] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-156] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-121] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-169] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-176] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-109] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_295'; source metadata written as null.

</details>