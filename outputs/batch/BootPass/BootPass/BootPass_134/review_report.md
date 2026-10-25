# Play-Annotation-Generator Annotation Review — BootPass_134

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_134`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_RunFlatRoute` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_BootAway` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | RT | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 42 | START | 42 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `10` | `10` | 50 | START | 57 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `11` | `11` | 50 | START | 50 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `12` | `12` | 50 | START | 50 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `15` | `15` | 50 | START | 50 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `17` | `17` | 50 | START | 50 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 56 | END | 42 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | `14` | `14` | 67 | START | 67 | 89 |
| ✅ EXACT | `Action_RunFlatRoute` | RT | `15` | `15` | 91 | START | 91 | 112 |
| ✅ EXACT | `Action_BootAway` | LT | `12` | `12` | 94 | START | 94 | 109 |
| ✅ EXACT | `Action_ThrowPass` | LT | `12` | `12` | 111 | START | 111 | 120 |
| ✅ EXACT | `Action_SecureCatch` | RT | `15` | `15` | 113 | START | 113 | 144 |

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
- **Visible Frames:** 0–123
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 56 | 15 | inferred_complete_timeline |
| `Action_None` | 57 | 66 | 10 | inferred_complete_timeline |
| `Action_FakeHandoff` | 67 | 89 | 23 | inferred_complete_timeline |
| `Action_FakeHandoff` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 120 | 27 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 108 | 67 | inferred_complete_timeline |
| `Action_None` | 110 | 225 | 116 | inferred_complete_timeline |
| `Action_None` | 227 | 233 | 7 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–8
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 66 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 71 | 22 | inferred_complete_timeline |
| `Action_RunBlock` | 82 | 93 | 12 | inferred_complete_timeline |
| `Action_BootAway` | 94 | 109 | 16 | inferred_complete_timeline |
| `Action_None` | 110 | 110 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 111 | 120 | 10 | inferred_complete_timeline |
| `Action_None` | 121 | 269 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 88 | 39 | inferred_complete_timeline |
| `Action_RunBlock` | 115 | 206 | 92 | inferred_complete_timeline |
| `Action_RunBlock` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_BallSnap` | 42 | 56 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 70 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 62 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 70 | 85 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 91 | 93 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 81 | 32 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 91 | 112 | 22 | inferred_complete_timeline |
| `Action_SecureCatch` | 113 | 144 | 32 | inferred_complete_timeline |
| `Action_None` | 145 | 213 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 44 | 118 | 75 | inferred_complete_timeline |
| `Action_None` | 120 | 126 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 233 | 97 | inferred_complete_timeline |
| `Action_None` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 41 | 10 | inferred_complete_timeline |
| `Action_None` | 42 | 81 | 40 | inferred_complete_timeline |
| `Action_None` | 92 | 117 | 26 | inferred_complete_timeline |
| `Action_None` | 119 | 144 | 26 | inferred_complete_timeline |
| `Action_None` | 157 | 226 | 70 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_None` | 42 | 106 | 65 | inferred_complete_timeline |
| `Action_None` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 250 | 134 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 41 | 25 | inferred_complete_timeline |
| `Action_None` | 42 | 90 | 49 | inferred_complete_timeline |
| `Action_None` | 93 | 98 | 6 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 58 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 42 | 230 | 189 | inferred_complete_timeline |
| `Action_None` | 233 | 258 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 244 | 203 | inferred_complete_timeline |
| `Action_None` | 255 | 259 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 202 | 161 | inferred_complete_timeline |
| `Action_None` | 204 | 269 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 11–269 | 252 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 50–81 | 32 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 55–250 | 173 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 77–117 | 4 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 83–99 | 17 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 110–228 | 119 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 124–166 | 43 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 139–151 | 10 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 141–269 | 129 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 150–269 | 119 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 152–269 | 100 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 170–269 | 100 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 176–269 | 94 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 188–204 | 17 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 195–269 | 74 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 210–269 | 60 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 215–269 | 55 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 237–269 | 33 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 242–269 | 27 | 2 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [42–56], lower_priority='Action_RunBlock' annotated_start=50, effective_Action_RunBlock_start=57.
- ⚠️ Action 'Action_None' range [42-244] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-58] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-230] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 42, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [42-42] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-118] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-233] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-108] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-225] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-117] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [57-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [87-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [95-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [107-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-62] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [70-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [91-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [67-89] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-81] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-213] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-66] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [115-206] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [208-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-222] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-224] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-228] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-168] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-191] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-204] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-227] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-269] for track '37' has 1 frames without a visible bounding box.
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