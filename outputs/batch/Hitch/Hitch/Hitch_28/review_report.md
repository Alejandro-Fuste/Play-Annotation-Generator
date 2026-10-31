# Play-Annotation-Generator Annotation Review — Hitch_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_28`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_RunHitchRoute` | WR4 | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_BallCarry` | WR4 | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `18` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 18 | START | 18 | 30 |
| ✅ EXACT | `Action_PassBlock` | LG | `15` | `15` | 21 | START | 21 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 21 | START | 21 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 21 | START | 21 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 21 | START | 21 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `9` | `9` | 21 | START | 31 | 50 |
| ✅ EXACT | `Action_RunHitchRoute` | WR4 | `18` | `18` | 30 | START | 30 | 100 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 30 | END | 18 | 30 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 74 | START | 74 | 78 |
| ✅ EXACT | `Action_BallCarry` | WR4 | `18` | `18` | 126 | START | 126 | 153 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 30 | 13 | inferred_complete_timeline |
| `Action_None` | 31 | 73 | 43 | inferred_complete_timeline |
| `Action_ThrowPass` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 50 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 30 | 100 | 71 | inferred_complete_timeline |
| `Action_None` | 101 | 125 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 153 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 50 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 77 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 50 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 30 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 50 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 56 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 50 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 50 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 155 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 157 | 190 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 52 | 35 | inferred_complete_timeline |
| `Action_None` | 131 | 164 | 34 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 177 | 8 | inferred_complete_timeline |
| `Action_None` | 180 | 190 | 11 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 52 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 52 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 52 | 35 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 192 | 175 | inferred_complete_timeline |
| `Action_None` | 194 | 204 | 11 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 168 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 26–29 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 40–41 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 42–43 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 99–210 | 83 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 128–210 | 74 | 6 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 130–131 | 2 | 1 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 132–210 | 76 | 2 | Undefined position; Undefined team |
| `29` | `29` | Position_Unknown | Team_Unknown | 143–210 | 57 | 2 | Undefined position; Undefined team |
| `30` | `30` | Position_Unknown | Team_Unknown | 146–210 | 59 | 2 | Undefined position; Undefined team |
| `31` | `31` | Position_Unknown | Team_Unknown | 146–210 | 62 | 3 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 146–210 | 38 | 6 | Undefined position; Undefined team |
| `33` | `34` | Position_Unknown | Team_Unknown | 148–210 | 56 | 2 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 161–210 | 50 | 1 | Undefined position; Undefined team |
| `35` | `37` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 170–210 | 38 | 3 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 184–186 | 3 | 1 | Undefined position; Undefined team |
| `38` | `41` | Position_Unknown | Team_Unknown | 195–210 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 38: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [18–30], lower_priority='Action_PassBlock' annotated_start=21, effective_Action_PassBlock_start=31.
- ⚠️ Action 'Action_None' range [18-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-52] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-52] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-192] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-52] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-164] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-57] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [74-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-52] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-25] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-50] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-29] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-155] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [157-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [192-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-29] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-205] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-205] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>