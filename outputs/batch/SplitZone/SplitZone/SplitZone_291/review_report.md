# Play-Annotation-Generator Annotation Review — SplitZone_291

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_291`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 141
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | SAF1 | defense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 9 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 17 | START | 17 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `10` | 24 | START | 24 | 53 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `11` | 24 | START | 31 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `13` | 24 | START | 24 | 92 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 24 | START | 24 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `9` | 24 | START | 24 | 52 |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | `16` | `15` | 26 | START | 26 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `15` | `14` | 30 | END | 21 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `12` | `12` | 34 | START | 34 | 52 |
| ✅ EXACT | `Action_Handoff` | SAF1 | `5` | `5` | 41 | START | 41 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 60 | START | 60 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `11` | `11` | 72 | START | 72 | 83 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–239
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 14 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 31 | 49 | 19 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 60 | 89 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 99 | 164 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PressEdge` | 34 | 52 | 19 | inferred_complete_timeline |
| `Action_PressEdge` | 55 | 97 | 43 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 92 | 69 | inferred_complete_timeline |
| `Action_None` | 93 | 176 | 84 | inferred_complete_timeline |
| `Action_None` | 179 | 188 | 10 | inferred_complete_timeline |
| `Action_None` | 191 | 195 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 52 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 92 | 10 | inferred_complete_timeline |
| `Action_None` | 93 | 159 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 71 | 41 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 72 | 83 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 142 | 49 | inferred_complete_timeline |
| `Action_None` | 144 | 200 | 57 | inferred_complete_timeline |
| `Action_None` | 202 | 220 | 19 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 53 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 92 | 1 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 51 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 66 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 87 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 118 | 30 | inferred_complete_timeline |
| `Action_None` | 120 | 167 | 48 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 133 | 117 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 149 | 164 | 16 | inferred_complete_timeline |
| `Action_None` | 168 | 177 | 10 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 131 | 115 | inferred_complete_timeline |
| `Action_None` | 133 | 151 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 99 | 83 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 131 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_Handoff` | 41 | 60 | 20 | inferred_complete_timeline |
| `Action_None` | 61 | 70 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 161 | 145 | inferred_complete_timeline |
| `Action_None` | 165 | 170 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 22–31 | 10 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 31–102 | 64 | 5 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 71–94 | 23 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 78–212 | 129 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 79–99 | 21 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 86–239 | 154 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 86–99 | 14 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 113–239 | 106 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 113–237 | 124 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 128–226 | 66 | 5 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 163–171 | 9 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 169–205 | 28 | 4 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 175–177 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 178–239 | 61 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 183–239 | 57 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 199–239 | 37 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 227–229 | 3 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 233–237 | 5 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (5 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 24 != Inferred start 31
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 584: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [17–30], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=31.
- ⚠️ Action 'Action_None' range [17-131] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-66] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-99] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-87] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-118] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-167] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [41-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-70] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-51] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-131] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [72-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-220] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [34-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-188] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-14] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [21-27] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [99-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-170] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [177-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [26-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-48] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-90] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-99] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-209] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>