# Play-Annotation-Generator Annotation Review — DeepCross_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_31`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 126
- **Validation Warnings:** 159
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 107
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 2 | START | 2 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 5 | START | 18 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 5 | START | 5 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 5 | START | 5 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 5 | START | 5 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 5 | START | 5 | 69 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | `0` | `0` | 17 | START | 17 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 17 | END | 2 | 17 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 95 | START | 95 | 103 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_None` | 18 | 94 | 77 | inferred_complete_timeline |
| `Action_ThrowPass` | 95 | 103 | 9 | inferred_complete_timeline |
| `Action_None` | 106 | 112 | 7 | inferred_complete_timeline |
| `Action_None` | 117 | 171 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 51 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 17 | 173 | 157 | inferred_complete_timeline |
| `Action_None` | 174 | 185 | 12 | inferred_complete_timeline |
| `Action_None` | 187 | 205 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 124 | 123 | inferred_complete_timeline |
| `Action_None` | 126 | 154 | 29 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 84 | 80 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 167 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 41 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 101 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 163 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 98 | 81 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 47 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 210 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 69 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 104 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 58 | 57 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 116 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 29 | 28 | inferred_complete_timeline |
| `Action_None` | 32 | 112 | 81 | inferred_complete_timeline |
| `Action_None` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_None` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_None` | 154 | 170 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 124 | 123 | inferred_complete_timeline |
| `Action_None` | 137 | 210 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 124 | 123 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 149 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–189 | 190 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 76–210 | 135 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 78–174 | 78 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 80–81 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 99–114 | 12 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 109–143 | 34 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 114–129 | 11 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 115–137 | 18 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 120–131 | 12 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 121–135 | 15 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 124–181 | 44 | 5 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 126–138 | 12 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 131–189 | 52 | 2 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 133–147 | 4 | 2 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 136–203 | 61 | 2 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 136–148 | 7 | 3 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 136–143 | 7 | 2 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 143–152 | 7 | 2 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 144–179 | 36 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 144–167 | 20 | 3 | Undefined position; Undefined team |
| `43` | `71` | Position_Unknown | Team_Unknown | 159–210 | 45 | 4 | Undefined position; Undefined team |
| `44` | `78` | Position_Unknown | Team_Unknown | 164–170 | 7 | 1 | Undefined position; Undefined team |
| `45` | `80` | Position_Unknown | Team_Unknown | 172–210 | 32 | 3 | Undefined position; Undefined team |
| `46` | `81` | Position_Unknown | Team_Unknown | 172–175 | 4 | 1 | Undefined position; Undefined team |
| `47` | `87` | Position_Unknown | Team_Unknown | 193–210 | 18 | 1 | Undefined position; Undefined team |
| `48` | `91` | Position_Unknown | Team_Unknown | 203–210 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 34: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [2–17], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=18.
- ⚠️ Action 'Action_None' range [174-185] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-116] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-29] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-112] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-145] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-170] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-58] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-154] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-124] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [95-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-171] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-167] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-37] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-51] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-104] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-119] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-147] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-174] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-137] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-177] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-131] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-138] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-175] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-191] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-179] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-167] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-170] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-188] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '48' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>