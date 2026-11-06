# Play-Annotation-Generator Annotation Review — OutsideZoneRead_105

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_105`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | SAF | defense | `17` | `16` |
| ✅ EXACT | `Action_ReadEdgeDefender` | SAF | defense | `17` | `16` |
| ✅ EXACT | `Action_Keep` | SAF | defense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | SAF | defense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 3 | START | 3 | 18 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `14` | 6 | START | 19 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 6 | START | 6 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `22` | `21` | 6 | START | 6 | 10 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 6 | START | 6 | 64 |
| ✅ EXACT | `Action_SnapReceive` | SAF | `17` | `16` | 18 | END | 3 | 18 |
| ✅ EXACT | `Action_ReadEdgeDefender` | SAF | `17` | `16` | 22 | START | 22 | 24 |
| ✅ EXACT | `Action_Keep` | SAF | `17` | `16` | 25 | START | 25 | 40 |
| ✅ EXACT | `Action_BallCarry` | SAF | `17` | `16` | 41 | START | 41 | 235 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 64 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 159 | 157 | inferred_complete_timeline |
| `Action_None` | 164 | 239 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 193 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 64 | 59 | inferred_complete_timeline |
| `Action_None` | 65 | 82 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 18 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 64 | 46 | inferred_complete_timeline |
| `Action_None` | 65 | 74 | 10 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 99 | 7 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 143 | 25 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 64 | 35 | inferred_complete_timeline |
| `Action_None` | 65 | 239 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 10 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 64 | 52 | inferred_complete_timeline |
| `Action_None` | 65 | 93 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 29 | 27 | inferred_complete_timeline |
| `Action_None` | 32 | 72 | 41 | inferred_complete_timeline |
| `Action_None` | 74 | 144 | 71 | inferred_complete_timeline |
| `Action_None` | 146 | 239 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 40 | 117 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 44 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 59 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_None` | 67 | 74 | 8 | inferred_complete_timeline |
| `Action_None` | 88 | 164 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 199 | 197 | inferred_complete_timeline |
| `Action_None` | 215 | 239 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 97 | 95 | inferred_complete_timeline |
| `Action_None` | 106 | 117 | 12 | inferred_complete_timeline |
| `Action_None` | 129 | 156 | 28 | inferred_complete_timeline |
| `Action_None` | 160 | 186 | 27 | inferred_complete_timeline |
| `Action_None` | 189 | 239 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 18 | 16 | inferred_complete_timeline |
| `Action_None` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 22 | 24 | 3 | inferred_complete_timeline |
| `Action_Keep` | 25 | 40 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 41 | 235 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–237 | 238 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 51–60 | 7 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 67–239 | 157 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 97–239 | 135 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 114–239 | 126 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 121–239 | 116 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 123–239 | 114 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 129–239 | 104 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 167–239 | 71 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 175–179 | 5 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 6 != Inferred start 19
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 212: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 212: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=19.
- ⚠️ Action 'Action_None' range [3-193] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-82] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-29] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-144] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-110] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-239] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-44] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-237] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-117] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 65, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [65-74] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [41-235] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-164] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-103] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-239] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-134] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-213] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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