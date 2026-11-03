# Play-Annotation-Generator Annotation Review — Slants0to10_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_71`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_PassBlock` | LT | `12` | `12` | 4 | START | 4 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 4 | START | 4 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 4 | START | 4 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 4 | START | 4 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 4 | START | 4 | 29 |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | `14` | `14` | 11 | START | 11 | 78 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 11 | END | 11 | 11 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 41 | START | 41 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `14` | `14` | 94 | START | 94 | 139 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 11 | 1 | inferred_complete_timeline |
| `Action_None` | 12 | 40 | 29 | inferred_complete_timeline |
| `Action_ThrowPass` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_None` | 52 | 71 | 20 | inferred_complete_timeline |
| `Action_None` | 86 | 119 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 11 | 78 | 68 | inferred_complete_timeline |
| `Action_None` | 79 | 93 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 139 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 220 | 80 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 239 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 111 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 196 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 32 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 29 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 148 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 8 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 15 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 24 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 32 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 39 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 24 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 32 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 239 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 175 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 237 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 49 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 239 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 168 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 174 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 183 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 191 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 239 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 224 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–148 | 139 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–20 | 17 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 79–239 | 151 | 7 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 87–132 | 42 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 89–239 | 117 | 10 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 113–239 | 123 | 4 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 125–128 | 4 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 127–196 | 48 | 2 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 129–142 | 12 | 3 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 134–141 | 8 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 153–239 | 87 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 159–182 | 24 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 165–239 | 73 | 2 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 175–208 | 34 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 191–239 | 46 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 72: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-224] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-148] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-168] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-183] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-196] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-32] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [141-220] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-175] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-62] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-32] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-32] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-119] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-8] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-29] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-148] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-15] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-126] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-133] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-156] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-110] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-130] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-170] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-122] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-156] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-239] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-128] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-132] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-130] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-137] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-142] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-141] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-182] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-171] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-208] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-234] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>