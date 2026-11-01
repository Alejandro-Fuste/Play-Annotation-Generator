# Play-Annotation-Generator Annotation Review — InsideZoneRead_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_85`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 6 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 62 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `16` | `15` | 28 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `16` | `15` | 31 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 42 | END | 28 | 42 |
| ✅ EXACT | `Action_ReadDefender` | QB | `13` | `12` | 49 | START | 49 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `13` | `12` | 58 | START | 58 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 71 | START | 71 | 139 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 122 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–101
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_None` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 49 | 57 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 60 | 70 | 11 | inferred_complete_timeline |
| `Action_None` | 71 | 83 | 13 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 139 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 149 | 153 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 190 | 6 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 61 | 34 | inferred_complete_timeline |
| `Action_None` | 63 | 67 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 114 | 87 | inferred_complete_timeline |
| `Action_None` | 118 | 127 | 10 | inferred_complete_timeline |
| `Action_None` | 131 | 163 | 33 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–15
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 15 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 65 | 38 | inferred_complete_timeline |
| `Action_None` | 82 | 97 | 16 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_None` | 44 | 49 | 6 | inferred_complete_timeline |
| `Action_None` | 51 | 53 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 53 | 26 | inferred_complete_timeline |
| `Action_None` | 56 | 65 | 10 | inferred_complete_timeline |
| `Action_None` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_None` | 90 | 94 | 5 | inferred_complete_timeline |
| `Action_None` | 96 | 101 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_None` | 111 | 114 | 4 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_None` | 135 | 150 | 16 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 193 | 166 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 122 | 95 | inferred_complete_timeline |
| `Action_None` | 127 | 136 | 10 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 109 | 82 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 124 | 210 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 131 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 164 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 22–44 | 21 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 48–135 | 27 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 54–210 | 157 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 74–210 | 137 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 79–210 | 96 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 89–123 | 23 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 116–150 | 35 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 147–181 | 31 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 179–210 | 32 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 183–210 | 28 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 186–210 | 20 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `16` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=28, end=15. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=31, end=15. Clamping end to start.
- ⚠️ Action 'Action_None' range [28-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-131] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-114] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-163] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-139] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [149-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [161-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-190] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-193] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' for track '12' starts at frame 58, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Handoff' range [58-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-65] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-101] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-166] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-102] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-171] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '27' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>