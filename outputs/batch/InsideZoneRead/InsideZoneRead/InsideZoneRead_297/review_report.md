# Play-Annotation-Generator Annotation Review — InsideZoneRead_297

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_297`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ⚠️ END CHANGED | `Action_SnapReceive` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `16` | `15` | 11 | START | 11 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 14 | START | 14 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 14 | START | 14 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 14 | START | 14 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 14 | START | 24 | 28 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `8` | `7` | 14 | START | N/A | N/A |
| ⚠️ END CHANGED | `Action_SnapReceive` | RT | `8` | `7` | 26 | END | 11 | 24 |
| ✅ EXACT | `Action_ReadDefender` | RT | `8` | `7` | 30 | START | 30 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | RT | `8` | `7` | 38 | START | 38 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | `8` | `7` | 64 | START | 64 | 95 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 94 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 95 | 85 | inferred_complete_timeline |
| `Action_None` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_None` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_None` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_None` | 141 | 151 | 11 | inferred_complete_timeline |
| `Action_None` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 202 | 15 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 40 | 30 | inferred_complete_timeline |
| `Action_None` | 44 | 96 | 53 | inferred_complete_timeline |
| `Action_None` | 99 | 176 | 78 | inferred_complete_timeline |
| `Action_None` | 187 | 193 | 7 | inferred_complete_timeline |
| `Action_None` | 201 | 210 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 101 | 91 | inferred_complete_timeline |
| `Action_None` | 105 | 210 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 92 | 82 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 94 | 81 | inferred_complete_timeline |
| `Action_None` | 95 | 210 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 54 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 28 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 67 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 28 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 94 | 65 | inferred_complete_timeline |
| `Action_None` | 95 | 210 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 24 | 14 | inferred_complete_timeline |
| `Action_None` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 30 | 37 | 8 | inferred_complete_timeline |
| `Action_Keep` | 38 | 55 | 18 | inferred_complete_timeline |
| `Action_Keep` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 64 | 95 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 124 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 134 | 8 | inferred_complete_timeline |

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
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 87 | 77 | inferred_complete_timeline |
| `Action_None` | 92 | 210 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 54 | 44 | inferred_complete_timeline |
| `Action_None` | 56 | 107 | 52 | inferred_complete_timeline |
| `Action_None` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 210 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_None` | 27 | 41 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 56 | 46 | inferred_complete_timeline |
| `Action_None` | 58 | 210 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 161 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 99 | 89 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 54–210 | 157 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 63–73 | 11 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 69–210 | 142 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 83–85 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 125–192 | 24 | 6 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 138–210 | 70 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 142–210 | 69 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 161–162 | 2 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 186–207 | 12 | 4 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `8` (RT)
- ⚠️ Ambiguous match for action `Action_Keep` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '7' has invalid range: start=14, end=10. Clamping end to start.
- ⚠️ Action 'Action_None' range [11-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-107] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-96] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-176] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [11-24] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [38-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [64-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-124] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-134] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-202] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-41] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-28] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-67] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-73] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-196] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_297'; source metadata written as null.

</details>