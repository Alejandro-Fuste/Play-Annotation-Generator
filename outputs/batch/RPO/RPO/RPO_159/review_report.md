# Play-Annotation-Generator Annotation Review — RPO_159

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_159`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `8` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 26 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `15` | 28 | START | 30 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `17` | 28 | START | 28 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 28 | START | 76 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 28 | START | 40 | 46 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `21` | `21` | 28 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `11` | `11` | 35 | START | 35 | 35 |
| ✅ EXACT | `Action_PullBall` | QB | `11` | `11` | 47 | START | 47 | 53 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 81 | START | 81 | 89 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 34 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 35 | 35 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_PullBall` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_None` | 54 | 80 | 27 | inferred_complete_timeline |
| `Action_ThrowPass` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_None` | 90 | 158 | 69 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 34 | 8 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 199 | 173 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 66 | 40 | inferred_complete_timeline |
| `Action_None` | 71 | 127 | 57 | inferred_complete_timeline |
| `Action_None` | 130 | 142 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 81 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_None` | 90 | 159 | 70 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_None` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–22
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 22 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 32 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 46 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 61 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 130 | 41 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_None` | 171 | 205 | 35 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 46 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 89 | 1 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 122 | 19 | inferred_complete_timeline |
| `Action_None` | 124 | 140 | 17 | inferred_complete_timeline |
| `Action_None` | 142 | 210 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 37 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_None` | 34 | 132 | 99 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 156 | 16 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_None` | 34 | 57 | 24 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 62 | 36 | inferred_complete_timeline |
| `Action_None` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_None` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 99 | 73 | inferred_complete_timeline |
| `Action_None` | 101 | 109 | 9 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 102 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 194 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 204 | 178 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 50–210 | 136 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 65–90 | 25 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 115–210 | 89 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 127–210 | 84 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 130–210 | 81 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 133–210 | 78 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 135–156 | 22 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 135–210 | 65 | 6 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 184–210 | 24 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 28 != Inferred start 30
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (LG)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=28, end=22. Clamping end to start.
- ⚠️ Action 'Action_None' range [27-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-204] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-194] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-37] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-62] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-41] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' for track '11' starts at frame 35, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ReadDefender' range [35-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-132] for track '13' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-156] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-66] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-46] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 90, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [90-93] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-57] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-61] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-130] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-100] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-85] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-156] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-173] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '31' has 1 frames without a visible bounding box.
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

</details>