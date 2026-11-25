# Play-Annotation-Generator Annotation Review — InsideZoneRead_363

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_363`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 111
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB2 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | DE2 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DE2 | defense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE2 | defense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_BallSnap` | LB2 | `12` | `11` | 26 | START | 26 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 29 | START | 29 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 29 | START | 29 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `16` | 29 | START | 29 | 88 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `17` | 29 | START | 29 | 92 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `22` | `21` | 29 | START | 29 | 101 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `13` | `12` | 40 | END | 26 | 40 |
| ✅ EXACT | `Action_ReadDefender` | DE2 | `13` | `12` | 44 | START | 44 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DE2 | `13` | `12` | 50 | START | 50 | 53 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE2 | `13` | `12` | 79 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 101 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 86 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 87 | 62 | inferred_complete_timeline |
| `Action_None` | 90 | 165 | 76 | inferred_complete_timeline |
| `Action_None` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 210 | 31 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 210 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 210 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 210 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 88 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 133 | 30 | inferred_complete_timeline |
| `Action_None` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_None` | 185 | 204 | 20 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 61 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 73 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 68 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 97 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 102 | 151 | 50 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 190 | 10 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 92 | 64 | inferred_complete_timeline |
| `Action_None` | 104 | 151 | 48 | inferred_complete_timeline |
| `Action_None` | 153 | 164 | 12 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 101 | 73 | inferred_complete_timeline |
| `Action_None` | 102 | 148 | 47 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 151 | 126 | inferred_complete_timeline |
| `Action_None` | 155 | 176 | 22 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_None` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 44 | 49 | 6 | inferred_complete_timeline |
| `Action_Keep` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_Keep` | 56 | 57 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 91 | 66 | inferred_complete_timeline |
| `Action_None` | 93 | 162 | 70 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |
| `Action_None` | 185 | 210 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 53 | 28 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 91 | 66 | inferred_complete_timeline |
| `Action_None` | 93 | 99 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 164 | 63 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 196 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_None` | 41 | 87 | 47 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 103 | 151 | 49 | inferred_complete_timeline |
| `Action_None` | 155 | 166 | 12 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 210 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 210 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 210 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 102 | 77 | inferred_complete_timeline |
| `Action_None` | 105 | 210 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 195 | 170 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 210 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–175 | 176 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 48–97 | 46 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 66–82 | 17 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 87–210 | 106 | 6 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 107–210 | 104 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 111–210 | 99 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 114–148 | 33 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 189–210 | 22 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `13` (DE2)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 725: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '12' has invalid range: start=79, end=57. Clamping end to start.
- ⚠️ Action 'Action_None' range [26-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-165] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-195] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-91] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-164] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-196] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-151] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-166] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [50-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [56-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-133] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-204] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-164] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-176] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-91] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-162] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-53] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-142] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_363'; source metadata written as null.

</details>