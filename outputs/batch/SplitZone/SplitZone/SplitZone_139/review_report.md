# Play-Annotation-Generator Annotation Review — SplitZone_139

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_139`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | defense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 5 | START | 6 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 5 | START | 6 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 5 | START | 6 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 5 | START | 6 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 5 | START | 6 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 5 | START | 6 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 5 | START | 6 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 5 | START | 6 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 5 | START | 6 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 5 | START | 6 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 5 | START | 6 | 53 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 44 | START | 44 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 47 | START | 60 | 65 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `13` | 47 | START | 47 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 47 | START | 47 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 47 | START | 47 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 47 | START | 47 | 121 |
| ✅ EXACT | `Action_SplitBlock` | TE | `9` | `9` | 54 | START | 54 | 200 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 59 | END | 44 | 59 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | `18` | `18` | 92 | START | 92 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `12` | `12` | 103 | START | 103 | 160 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 59 | 16 | inferred_complete_timeline |
| `Action_None` | 60 | 102 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 160 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 163 | 329 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 113 | 70 | inferred_complete_timeline |
| `Action_None` | 118 | 329 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–320
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 154 | 111 | inferred_complete_timeline |
| `Action_None` | 164 | 320 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 329 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 141 | 98 | inferred_complete_timeline |
| `Action_None` | 150 | 252 | 103 | inferred_complete_timeline |
| `Action_None` | 256 | 273 | 18 | inferred_complete_timeline |
| `Action_None` | 281 | 329 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 53 | 48 | inferred_complete_timeline |
| `Action_SplitBlock` | 54 | 200 | 147 | inferred_complete_timeline |
| `Action_None` | 201 | 228 | 28 | inferred_complete_timeline |
| `Action_None` | 231 | 285 | 55 | inferred_complete_timeline |
| `Action_None` | 287 | 329 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 46 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 200 | 154 | inferred_complete_timeline |
| `Action_None` | 201 | 329 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 6–90
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 46 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 90 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 6–75
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_BallSnap` | 44 | 59 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 65 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 75 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 46 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 200 | 106 | inferred_complete_timeline |
| `Action_None` | 201 | 329 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 46 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 121 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 200 | 66 | inferred_complete_timeline |
| `Action_None` | 201 | 329 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 90 | 47 | inferred_complete_timeline |
| `Action_None` | 92 | 198 | 107 | inferred_complete_timeline |
| `Action_None` | 200 | 329 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 329 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 91 | 86 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 92 | 200 | 109 | inferred_complete_timeline |
| `Action_None` | 201 | 278 | 78 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 291 | 329 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 329 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 95 | 52 | inferred_complete_timeline |
| `Action_None` | 97 | 136 | 40 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 329 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 329 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 6–186
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 173 | 130 | inferred_complete_timeline |
| `Action_None` | 181 | 186 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 329 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 6–170
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 170 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–250
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 182 | 139 | inferred_complete_timeline |
| `Action_None` | 184 | 193 | 10 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 208 | 4 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 98–329 | 205 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 139–329 | 191 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 159–163 | 5 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 181–207 | 4 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 181–329 | 141 | 4 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 203–329 | 126 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 226–329 | 104 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 269–271 | 3 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 284–329 | 22 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [44–59], lower_priority='Action_ZoneBlock' annotated_start=47, effective_Action_ZoneBlock_start=60.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 154 frames exceeds threshold 90 frames [start=47, end=200].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '18' (DT1) duration 109 frames exceeds threshold 90 frames [start=92, end=200].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 154 frames exceeds threshold 90 frames [start=47, end=200].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 154 frames exceeds threshold 90 frames [start=47, end=200].
- ⚠️ Action 'Action_None' range [44-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-320] for track '0' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-141] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-252] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-273] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-170] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-182] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-228] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-285] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-329] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-65] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [163-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-113] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-278] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-329] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-229] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '33' has 1 frames without a visible bounding box.
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

</details>