# Play-Annotation-Generator Annotation Review — Hitch_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_42`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_RunHitchRoute` | LB1 | defense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BallCarry` | LB1 | defense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 7 | START | 7 | 23 |
| ✅ EXACT | `Action_PassBlock` | LG | `14` | `14` | 10 | START | 10 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 10 | START | 24 | 30 |
| ✅ EXACT | `Action_PassBlock` | LT | `3` | `3` | 10 | START | 10 | 17 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `8` | 10 | START | 10 | 210 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 23 | END | 7 | 23 |
| ✅ EXACT | `Action_RunHitchRoute` | LB1 | `9` | `9` | 24 | START | 24 | 87 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 87 | START | 87 | 95 |
| ✅ EXACT | `Action_BallCarry` | LB1 | `9` | `9` | 119 | START | 119 | 138 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 23 | 17 | inferred_complete_timeline |
| `Action_None` | 24 | 86 | 63 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 95 | 9 | inferred_complete_timeline |
| `Action_None` | 96 | 182 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 156 | 150 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 57 | 51 | inferred_complete_timeline |
| `Action_None` | 59 | 144 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 191 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 173 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 17 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 53 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 23 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 36 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 55 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 112 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 51 | 45 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_None` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_None` | 71 | 84 | 14 | inferred_complete_timeline |
| `Action_None` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 108 | 113 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 45 | 39 | inferred_complete_timeline |
| `Action_None` | 47 | 90 | 44 | inferred_complete_timeline |
| `Action_None` | 100 | 176 | 77 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 183 | 200 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 51 | 45 | inferred_complete_timeline |
| `Action_None` | 59 | 69 | 11 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 118 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 119 | 138 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 27 | 21 | inferred_complete_timeline |
| `Action_None` | 30 | 71 | 42 | inferred_complete_timeline |
| `Action_None` | 90 | 100 | 11 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 184 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 188 | 182 | inferred_complete_timeline |
| `Action_None` | 190 | 195 | 6 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 205 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 7–188 | 181 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 24–210 | 187 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 52–203 | 137 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 113–117 | 5 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 115–197 | 83 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 125–210 | 86 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 169–201 | 27 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 180–193 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 52: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [7–23], lower_priority='Action_PassBlock' annotated_start=10, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_None' range [7-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-17] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-156] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [119-138] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-188] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-200] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-57] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-144] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-51] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-84] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-184] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-17] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-188] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-63] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-188] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.

</details>