# Play-Annotation-Generator Annotation Review — JetSweep_108

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_108`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 12 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 43 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 123 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `3` | `2` | 68 | START | 68 | 153 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 124 | START | 124 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `15` | `14` | 125 | START | 125 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 125 | START | 138 | 139 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `17` | `16` | 125 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 125 | START | 143 | 155 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 137 | END | 124 | 137 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 141 | START | 141 | 153 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `3` | `2` | 154 | START | 154 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 193 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_SnapReceive` | 124 | 137 | 14 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_Toss` | 141 | 153 | 13 | inferred_complete_timeline |
| `Action_None` | 154 | 230 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 200 | 77 | inferred_complete_timeline |
| `Action_None` | 216 | 269 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_JetMotion` | 68 | 153 | 86 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 269 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_LeadBlock` | 125 | 125 | 1 | inferred_complete_timeline |
| `Action_LeadBlock` | 142 | 183 | 42 | inferred_complete_timeline |
| `Action_None` | 195 | 211 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 12–122
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 16 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 75 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 122 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 124 | 134 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 161 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 193 | 20 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 43–224
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 43 | 61 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 67 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 118 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 155 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 193 | 31 | inferred_complete_timeline |
| `Action_None` | 194 | 224 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 12–122
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 16 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 122 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–120
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 120 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 256 | 133 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 170 | 47 | inferred_complete_timeline |
| `Action_None` | 173 | 269 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 247 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 211 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 262 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 12–269 | 185 | 10 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 126–213 | 73 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 147–269 | 123 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 148–266 | 118 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 154–215 | 62 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 156–269 | 108 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 208–213 | 6 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 215–228 | 11 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 225–269 | 45 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `17` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 218: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [124–137], lower_priority='Action_ZoneBlock' annotated_start=125, effective_Action_ZoneBlock_start=138.
- ⚠️ Segment 'Action_ZoneBlock' for track '16' has invalid range: start=125, end=122. Clamping end to start.
- ⚠️ Action 'Action_None' range [124-247] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-262] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-256] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [124-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-161] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-211] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' for track '14' starts at frame 125, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_LeadBlock' range [125-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [142-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-211] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-30] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-120] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-30] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-22] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-122] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-15] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-151] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-61] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-118] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-155] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-213] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-262] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.

</details>