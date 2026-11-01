# Play-Annotation-Generator Annotation Review — InsideZoneRead_129

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_129`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 21 | START | 21 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 24 | START | 24 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 24 | START | 34 | 39 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `20` | 24 | START | 24 | 87 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 24 | START | 24 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 24 | START | 24 | 44 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 33 | END | 21 | 33 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `16` | 36 | START | 36 | 48 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `18` | `17` | 47 | START | 47 | 60 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 49 | START | 49 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `20` | `19` | 56 | START | 56 | 103 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 87 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 36 | 48 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_None` | 56 | 194 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_BallCarry` | 56 | 103 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 105 | 156 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 176 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 200 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 190 | 170 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 145 | 125 | inferred_complete_timeline |
| `Action_None` | 147 | 210 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 44 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 202 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 46 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 47 | 60 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 39 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 55 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 44 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 79 | 31 | inferred_complete_timeline |
| `Action_None` | 112 | 209 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 112 | 25 | inferred_complete_timeline |
| `Action_None` | 114 | 139 | 26 | inferred_complete_timeline |

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
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 54 | 34 | inferred_complete_timeline |
| `Action_None` | 56 | 75 | 20 | inferred_complete_timeline |
| `Action_None` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_None` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_None` | 145 | 164 | 20 | inferred_complete_timeline |
| `Action_None` | 178 | 210 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_None` | 35 | 178 | 144 | inferred_complete_timeline |
| `Action_None` | 181 | 189 | 9 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 91 | 71 | inferred_complete_timeline |
| `Action_None` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 54 | 34 | inferred_complete_timeline |
| `Action_None` | 60 | 210 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 44 | 24 | inferred_complete_timeline |
| `Action_None` | 53 | 210 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 200 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 182 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 182 | 162 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 202 | 5 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 5–210 | 197 | 6 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 63–91 | 17 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 63–88 | 20 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 67–105 | 8 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 80–210 | 120 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 86–210 | 122 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 89–210 | 122 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 90–98 | 9 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 108–189 | 82 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 131–139 | 9 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 133–166 | 24 | 4 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (7 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [21–33], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=34.
- ⚠️ Action 'Action_None' range [21-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-200] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-44] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-87] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-202] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-27] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-182] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-44] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-79] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [47-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-39] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-55] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [105-156] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [158-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [161-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-200] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-112] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-139] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-74] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-96] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-198] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '33' has 2 frames without a visible bounding box.
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

</details>