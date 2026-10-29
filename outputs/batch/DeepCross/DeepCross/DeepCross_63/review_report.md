# Play-Annotation-Generator Annotation Review — DeepCross_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_63`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 107
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | SAF2 | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | CB1 | defense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `7` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | SAF2 | `14` | `14` | 17 | START | 17 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `11` | `11` | 20 | START | 20 | 45 |
| ✅ EXACT | `Action_PassBlock` | RG | `17` | `17` | 20 | START | 20 | 93 |
| ✅ EXACT | `Action_PassBlock` | RT | `19` | `19` | 20 | START | 20 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 20 | START | 20 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | CB1 | `18` | `18` | 32 | START | 32 | 78 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 32 | END | 17 | 32 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 121 | START | 121 | 129 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 32 | 16 | inferred_complete_timeline |
| `Action_None` | 33 | 106 | 74 | inferred_complete_timeline |
| `Action_None` | 120 | 120 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 121 | 129 | 9 | inferred_complete_timeline |
| `Action_None` | 130 | 143 | 14 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_None` | 156 | 161 | 6 | inferred_complete_timeline |
| `Action_None` | 163 | 172 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 190 | 174 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 132 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 69 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 104 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 132 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 147 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 172 | 205 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 101 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 116 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 130 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 185 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 188 | 199 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 93 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 141 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 104 | 88 | inferred_complete_timeline |
| `Action_None` | 106 | 134 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 143 | 127 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 103 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 134 | 118 | inferred_complete_timeline |
| `Action_None` | 136 | 141 | 6 | inferred_complete_timeline |
| `Action_None` | 146 | 194 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 143 | 127 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 160 | 12 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 32 | 78 | 47 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 91 | 185 | 95 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 193 | 4 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 105 | 89 | inferred_complete_timeline |
| `Action_None` | 122 | 143 | 22 | inferred_complete_timeline |
| `Action_None` | 145 | 207 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 102 | 86 | inferred_complete_timeline |
| `Action_None` | 106 | 110 | 5 | inferred_complete_timeline |
| `Action_None` | 112 | 141 | 30 | inferred_complete_timeline |
| `Action_None` | 143 | 149 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 174 | 158 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 196 | 14 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 129 | 113 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 32 | 16 | inferred_complete_timeline |
| `Action_None` | 33 | 47 | 15 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–210 | 194 | 4 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–76 | 77 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–210 | 209 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 56–64 | 8 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 92–126 | 35 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 94–196 | 102 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 114–134 | 20 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 124–210 | 78 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 159–161 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 160–210 | 43 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 170–210 | 41 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 180–210 | 24 | 5 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 182–183 | 2 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `41` | `45` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `42` | `46` | Position_Unknown | Team_Unknown | 202–206 | 5 | 1 | Undefined position; Undefined team |
| `43` | `48` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (9 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 66: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ Row 66: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 66: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 66: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [17-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-104] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-134] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-194] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-143] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-143] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-141] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-173] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-201] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-143] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-45] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-85] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-147] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [172-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [207-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-47] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-174] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-106] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [32-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [91-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-101] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [120-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [188-199] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-134] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-143] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-188] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-206] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>