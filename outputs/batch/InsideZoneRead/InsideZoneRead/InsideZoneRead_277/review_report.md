# Play-Annotation-Generator Annotation Review — InsideZoneRead_277

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_277`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB2 | defense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_Keep` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | CB2 | `8` | `7` | 10 | START | 10 | 27 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `16` | 13 | START | 13 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 13 | START | 13 | 57 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `20` | 13 | START | 13 | 36 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `7` | `6` | 13 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | C | `7` | `6` | 27 | END | 10 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | C | `7` | `6` | 30 | START | 30 | 32 |
| ✅ EXACT | `Action_Keep` | C | `7` | `6` | 40 | START | 40 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | `7` | `6` | 67 | START | 67 | 83 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 82 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–156
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 143 | 134 | inferred_complete_timeline |
| `Action_None` | 145 | 156 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 33 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 122 | 113 | inferred_complete_timeline |
| `Action_None` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_None` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_None` | 100 | 147 | 48 | inferred_complete_timeline |
| `Action_None` | 155 | 167 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 57 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 72 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 36 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 35 | 39 | 5 | inferred_complete_timeline |
| `Action_Keep` | 40 | 66 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 67 | 83 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 180 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 82 | 70 | inferred_complete_timeline |
| `Action_None` | 83 | 168 | 86 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 38 | 29 | inferred_complete_timeline |
| `Action_None` | 40 | 180 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 41 | 32 | inferred_complete_timeline |
| `Action_None` | 43 | 85 | 43 | inferred_complete_timeline |
| `Action_None` | 89 | 94 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 180 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 153 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 69 | 60 | inferred_complete_timeline |
| `Action_None` | 71 | 81 | 11 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 36 | 27 | inferred_complete_timeline |
| `Action_None` | 38 | 180 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 100 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 165 | 156 | inferred_complete_timeline |
| `Action_None` | 167 | 180 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 109 | 82 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 180 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 171 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 52–180 | 126 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 74–180 | 105 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 79–180 | 102 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 97–177 | 79 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 101–174 | 25 | 6 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 102–180 | 78 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 124–128 | 5 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 152–157 | 6 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 158–173 | 15 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 164–169 | 6 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 170–180 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (C)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 554: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '6' has invalid range: start=13, end=9. Clamping end to start.
- ⚠️ Action 'Action_None' range [10-41] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-85] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-147] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-167] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-38] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-180] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [30-32] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [67-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-36] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-57] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-72] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-166] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-109] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_277'; source metadata written as null.

</details>