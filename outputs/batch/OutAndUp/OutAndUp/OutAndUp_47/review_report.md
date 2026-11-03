# Play-Annotation-Generator Annotation Review — OutAndUp_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_47`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 123
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_SellOut` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_RunGoRoute` | WR2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `0` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `10` | `10` | 25 | START | 25 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `0` | `0` | 28 | START | 28 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `12` | `12` | 28 | START | 28 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 28 | START | 28 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `15` | `15` | 28 | START | 28 | 47 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 38 | END | 25 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_SellOut` | WR2 | `1` | `1` | 96 | START | 96 | 97 |
| ✅ EXACT | `Action_RunGoRoute` | WR2 | `1` | `1` | 126 | START | 126 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `19` | `19` | 131 | START | 131 | 132 |

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
- **Visible Frames:** 0–228
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 38 | 14 | inferred_complete_timeline |
| `Action_None` | 39 | 57 | 19 | inferred_complete_timeline |
| `Action_None` | 59 | 130 | 72 | inferred_complete_timeline |
| `Action_ThrowPass` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_None` | 144 | 144 | 1 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 228 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 78 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 54 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 95 | 37 | inferred_complete_timeline |
| `Action_SellOut` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_SellOut` | 102 | 125 | 24 | inferred_complete_timeline |
| `Action_RunGoRoute` | 126 | 144 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 273 | 249 | inferred_complete_timeline |
| `Action_None` | 279 | 282 | 4 | inferred_complete_timeline |
| `Action_None` | 284 | 299 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 48 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 78 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 86 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 47 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 71 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 78 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 80 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 299 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 48 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 78 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 86 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 57 | 33 | inferred_complete_timeline |
| `Action_None` | 61 | 86 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_None` | 63 | 82 | 20 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 229 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 70 | 78 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_None` | 60 | 71 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_None` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_None` | 40 | 78 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 68 | 44 | inferred_complete_timeline |
| `Action_None` | 70 | 241 | 172 | inferred_complete_timeline |
| `Action_None` | 244 | 279 | 36 | inferred_complete_timeline |
| `Action_None` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 172 | 148 | inferred_complete_timeline |
| `Action_None` | 179 | 237 | 59 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 207 | 183 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 144 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 144 | 120 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–86 | 76 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 17–18 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 29–69 | 37 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 85–167 | 81 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 89–144 | 52 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 107–299 | 193 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 119–144 | 21 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 119–125 | 6 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 119–125 | 5 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 138–150 | 11 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 145–292 | 144 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 145–295 | 111 | 7 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 145–161 | 17 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 145–235 | 91 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 151–299 | 149 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 179–299 | 121 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 202–299 | 68 | 9 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 205–207 | 3 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 213–299 | 87 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 236–293 | 37 | 5 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 286–299 | 7 | 2 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 296–298 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SellOut` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 109 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 49: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PassBlock' range [28-80] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-57] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellOut' range [96-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [126-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-57] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-71] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-273] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-68] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-241] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-279] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-78] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-78] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-144] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-37] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-78] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-172] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-237] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [131-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 144, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [144-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-212] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-250] for track '30' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-292] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-164] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-243] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-295] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-161] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-235] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-255] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-279] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-276] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>