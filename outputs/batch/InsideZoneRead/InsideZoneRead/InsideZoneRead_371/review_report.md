# Play-Annotation-Generator Annotation Review — InsideZoneRead_371

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_371`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 2
- **Action Segments:** 99
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | DT2 | defense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | DT2 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DT2 | defense | `12` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | CB2 | defense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | DT2 | defense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_BallSnap` | CB2 | `11` | `10` | 3 | START | 3 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 6 | START | 6 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `18` | 6 | START | 6 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 6 | START | 6 | 25 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 6 | START | 6 | 77 |
| ✅ EXACT | `Action_SnapReceive` | DT2 | `12` | `11` | 18 | END | 3 | 18 |
| ✅ EXACT | `Action_ReadDefender` | DT2 | `12` | `11` | 21 | START | 21 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DT2 | `12` | `11` | 27 | START | 27 | 32 |
| ✅ EXACT | `Action_BlockSecondLevel` | CB2 | `11` | `10` | 32 | START | 32 | 77 |
| ✅ EXACT | `Action_BallCarry` | DT2 | `12` | `11` | 59 | START | 59 | 185 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 77 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 59 | 57 | inferred_complete_timeline |
| `Action_None` | 63 | 210 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 175 | 173 | inferred_complete_timeline |
| `Action_None` | 178 | 209 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 46 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 180 | 130 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 139 | 137 | inferred_complete_timeline |
| `Action_None` | 150 | 152 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 77 | 72 | inferred_complete_timeline |
| `Action_None` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 77 | 72 | inferred_complete_timeline |
| `Action_None` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 25 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 77 | 72 | inferred_complete_timeline |
| `Action_None` | 78 | 110 | 33 | inferred_complete_timeline |
| `Action_None` | 124 | 210 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 35 | 33 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 40 | 38 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 18 | 16 | inferred_complete_timeline |
| `Action_None` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 21 | 26 | 6 | inferred_complete_timeline |
| `Action_Keep` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_Keep` | 35 | 42 | 8 | inferred_complete_timeline |
| `Action_Keep` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_Keep` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 59 | 185 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 204 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 18 | 16 | inferred_complete_timeline |
| `Action_None` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 32 | 77 | 46 | inferred_complete_timeline |
| `Action_None` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 177 | 175 | inferred_complete_timeline |
| `Action_None` | 183 | 207 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 101 | 99 | inferred_complete_timeline |
| `Action_None` | 103 | 183 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 184 | 182 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–34 | 26 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 50–210 | 161 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 52–210 | 143 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 90–210 | 117 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 113–132 | 18 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 137–210 | 70 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 144–181 | 18 | 3 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 165–178 | 7 | 2 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 172–210 | 39 | 1 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 178–210 | 13 | 3 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 182–190 | 6 | 2 | Undefined position; Undefined team |
| `34` | `57` | Position_Unknown | Team_Unknown | 185–195 | 10 | 2 | Undefined position; Undefined team |
| `35` | `58` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `36` | `65` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `27` | `36` | 143 | 160 | 14 | 77.8% | 156–159 |
| `37` | `66` | 207 | 208 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 742: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [3-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-204] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-177] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-40] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-139] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [27-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [35-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [52-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-210] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-23] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-209] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-25] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-63] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-130] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_371'; source metadata written as null.

</details>