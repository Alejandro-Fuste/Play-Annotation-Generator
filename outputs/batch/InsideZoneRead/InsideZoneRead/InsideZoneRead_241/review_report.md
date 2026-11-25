# Play-Annotation-Generator Annotation Review — InsideZoneRead_241

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_241`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | DT2 | defense | `15` | `14` |
| ✅ EXACT | `Action_ReadDefender` | DT2 | defense | `15` | `14` |
| ✅ EXACT | `Action_Keep` | DT2 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | defense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `10` | `9` | 4 | START | 4 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `12` | 7 | START | 7 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 7 | START | 7 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 7 | START | 7 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 7 | START | 7 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 7 | START | 7 | 75 |
| ✅ EXACT | `Action_SnapReceive` | DT2 | `15` | `14` | 18 | END | 4 | 18 |
| ✅ EXACT | `Action_ReadDefender` | DT2 | `15` | `14` | 22 | START | 22 | 34 |
| ✅ EXACT | `Action_Keep` | DT2 | `15` | `14` | 35 | START | 35 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | `15` | `14` | 48 | START | 48 | 51 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 75 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 179 | 176 | inferred_complete_timeline |
| `Action_None` | 183 | 210 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 186 | 183 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 65 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 22 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 43 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 40 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 50 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 75 | 69 | inferred_complete_timeline |
| `Action_None` | 76 | 138 | 63 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 75 | 69 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 33 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_None` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 22 | 34 | 13 | inferred_complete_timeline |
| `Action_Keep` | 35 | 47 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 85 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 77 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 210 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 140 | 137 | inferred_complete_timeline |
| `Action_None` | 151 | 175 | 25 | inferred_complete_timeline |
| `Action_None` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_None` | 19 | 148 | 130 | inferred_complete_timeline |
| `Action_None` | 150 | 210 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 90 | 87 | inferred_complete_timeline |
| `Action_None` | 96 | 186 | 91 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–210 | 208 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 31–210 | 172 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 63–210 | 112 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 96–210 | 115 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 104–128 | 16 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 123–210 | 88 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 178–199 | 22 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 179–181 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 185–200 | 8 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 198–201 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (4 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 482: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [4-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-50] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-62] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-148] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-179] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-186] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [48-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [57-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [61-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-22] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-43] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-59] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-152] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-167] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_241'; source metadata written as null.

</details>