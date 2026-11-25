# Play-Annotation-Generator Annotation Review — InsideZoneRead_269

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_269`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | TE1 | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | DT2 | defense | `19` | `18` |
| ✅ EXACT | `Action_ReadDefender` | DT2 | defense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE1 | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DT2 | defense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | defense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | TE1 | `17` | `16` | 1 | START | 1 | 13 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `17` | 4 | START | 4 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 4 | START | 4 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 4 | START | 4 | 70 |
| ✅ EXACT | `Action_ZoneBlock` | C | `22` | `21` | 4 | START | 4 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 4 | START | 4 | 71 |
| ✅ EXACT | `Action_SnapReceive` | DT2 | `19` | `18` | 13 | END | 1 | 13 |
| ✅ EXACT | `Action_ReadDefender` | DT2 | `19` | `18` | 19 | START | 19 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE1 | `17` | `16` | 30 | START | 30 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DT2 | `19` | `18` | 32 | START | 32 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | `19` | `18` | 49 | START | 49 | 56 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 71 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 52 | 52 | inferred_complete_timeline |
| `Action_None` | 56 | 184 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 104 | 104 | inferred_complete_timeline |
| `Action_None` | 110 | 135 | 26 | inferred_complete_timeline |
| `Action_None` | 137 | 210 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 127 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 14 | 29 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 30 | 40 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 42 | 46 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 50 | 71 | 22 | inferred_complete_timeline |
| `Action_None` | 72 | 81 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 71 | 68 | inferred_complete_timeline |
| `Action_None` | 72 | 210 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 70 | 67 | inferred_complete_timeline |
| `Action_None` | 72 | 79 | 8 | inferred_complete_timeline |
| `Action_None` | 88 | 91 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 71 | 68 | inferred_complete_timeline |
| `Action_None` | 72 | 210 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 71 | 68 | inferred_complete_timeline |
| `Action_None` | 72 | 200 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 71 | 68 | inferred_complete_timeline |
| `Action_None` | 72 | 210 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 88 | 88 | inferred_complete_timeline |
| `Action_None` | 90 | 112 | 23 | inferred_complete_timeline |
| `Action_None` | 115 | 210 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 49 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 146 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 64 | 64 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 14 | 18 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_Keep` | 32 | 40 | 9 | inferred_complete_timeline |
| `Action_Keep` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 162 | 162 | inferred_complete_timeline |
| `Action_None` | 164 | 210 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 89 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 192 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 209 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 172 | 172 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 39–210 | 161 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 42–210 | 124 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 74–75 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 74–95 | 16 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 85–210 | 126 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 110–115 | 6 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 119–210 | 92 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 153–163 | 11 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 179–182 | 4 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 182–200 | 12 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 60 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [1-52] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-88] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-135] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-71] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-127] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-64] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-209] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [30-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [42-46] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [50-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [32-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [49-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-83] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-163] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_269'; source metadata written as null.

</details>