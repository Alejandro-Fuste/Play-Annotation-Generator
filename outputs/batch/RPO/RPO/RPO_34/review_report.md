# Play-Annotation-Generator Annotation Review — RPO_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_34`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `20` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 4 | START | 4 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 4 | START | 4 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 4 | START | 4 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 4 | START | 4 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 4 | START | 4 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 4 | START | 4 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 4 | START | 4 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 4 | START | 4 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 4 | START | 4 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 4 | START | 4 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `16` | `16` | 28 | START | 28 | 65 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 28 | START | 28 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | C | `19` | `19` | 28 | START | 28 | 77 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `20` | `20` | 28 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 28 | START | 28 | 31 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `14` | 31 | START | 31 | 40 |
| ✅ EXACT | `Action_PullBall` | QB | `14` | `14` | 41 | START | 41 | 57 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 68 | START | 68 | 77 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–140
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 30 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 31 | 40 | 10 | inferred_complete_timeline |
| `Action_PullBall` | 41 | 57 | 17 | inferred_complete_timeline |
| `Action_None` | 58 | 67 | 10 | inferred_complete_timeline |
| `Action_ThrowPass` | 68 | 77 | 10 | inferred_complete_timeline |
| `Action_None` | 78 | 135 | 58 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 4–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 137 | 111 | inferred_complete_timeline |
| `Action_None` | 142 | 180 | 39 | inferred_complete_timeline |
| `Action_None` | 183 | 192 | 10 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 4–166
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 87 | 61 | inferred_complete_timeline |
| `Action_None` | 91 | 166 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–72
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 72 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–24
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 24 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 4–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 20 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_None` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 77 | 50 | inferred_complete_timeline |
| `Action_None` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 77 | 41 | inferred_complete_timeline |
| `Action_None` | 78 | 206 | 129 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 4–139
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 65 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 77 | 4 | inferred_complete_timeline |
| `Action_None` | 78 | 139 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 37 | 11 | inferred_complete_timeline |
| `Action_None` | 40 | 98 | 59 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 68 | 42 | inferred_complete_timeline |
| `Action_None` | 77 | 210 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–134
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 134 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–170
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 84 | 58 | inferred_complete_timeline |
| `Action_None` | 87 | 170 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 4–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 150 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–43
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 43 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–123
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 123 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 4–210 | 207 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 49–210 | 156 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 73–83 | 5 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 87–210 | 118 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 116–156 | 41 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 130–166 | 37 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 143–210 | 68 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 143–145 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 163–208 | 24 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 187–210 | 22 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 60: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=28, end=24. Clamping end to start.
- ⚠️ Action 'Action_None' range [27-87] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-37] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-98] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-210] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-72] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-77] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-81] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-208] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '32' has 1 frames without a visible bounding box.
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

</details>