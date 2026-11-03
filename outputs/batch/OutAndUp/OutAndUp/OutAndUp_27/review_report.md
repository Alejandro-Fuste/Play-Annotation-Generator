# Play-Annotation-Generator Annotation Review — OutAndUp_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_27`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 153
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 123
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_SellOut` | WR4 | offense | `2` | `2` |
| ✅ EXACT | `Action_RunGoRoute` | WR4 | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 12 | START | 12 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `1` | `1` | 15 | START | 15 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 15 | START | 15 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 15 | START | 15 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 15 | START | 25 | 34 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 24 | END | 12 | 24 |
| ✅ EXACT | `Action_SellOut` | WR4 | `2` | `2` | 54 | START | 54 | 76 |
| ✅ EXACT | `Action_RunGoRoute` | WR4 | `2` | `2` | 77 | START | 77 | 210 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 84 | START | 84 | 87 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 24 | 13 | inferred_complete_timeline |
| `Action_None` | 25 | 83 | 59 | inferred_complete_timeline |
| `Action_ThrowPass` | 84 | 87 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 58 | 47 | inferred_complete_timeline |
| `Action_None` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 182 | 108 | inferred_complete_timeline |
| `Action_None` | 185 | 191 | 7 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 74 | 63 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 84 | 87 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 45 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_None` | 57 | 66 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 58 | 47 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 80 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 159 | 74 | inferred_complete_timeline |
| `Action_None` | 164 | 188 | 25 | inferred_complete_timeline |
| `Action_None` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_SellOut` | 54 | 76 | 23 | inferred_complete_timeline |
| `Action_RunGoRoute` | 77 | 210 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 58 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 24 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 79 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 33 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 58 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 52 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 89 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 122 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 204 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_None` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 34 | 23 | inferred_complete_timeline |
| `Action_None` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 124 | 11 | inferred_complete_timeline |
| `Action_None` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_None` | 138 | 148 | 11 | inferred_complete_timeline |
| `Action_None` | 152 | 173 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 34 | 23 | inferred_complete_timeline |
| `Action_None` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 79 | 5 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 34 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_None` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 82 | 10 | inferred_complete_timeline |
| `Action_None` | 84 | 89 | 6 | inferred_complete_timeline |
| `Action_None` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_None` | 100 | 104 | 5 | inferred_complete_timeline |
| `Action_None` | 106 | 200 | 95 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 110 | 34 | inferred_complete_timeline |
| `Action_None` | 113 | 164 | 52 | inferred_complete_timeline |
| `Action_None` | 185 | 210 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 126 | 177 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–86 | 67 | 8 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 55–210 | 151 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 67–210 | 141 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 78–164 | 85 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 81–185 | 36 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 105–209 | 97 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 118–164 | 38 | 6 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 171–173 | 3 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 171–173 | 3 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 201–210 | 4 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 203–210 | 8 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 206–209 | 4 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 118 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 30: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [12–24], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=25.
- ⚠️ Action 'Action_None' range [12-34] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-34] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-52] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-58] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-68] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-71] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-89] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-122] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [129-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellOut' range [54-76] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [77-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-37] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-58] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-86] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-45] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-55] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-110] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-121] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-177] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-58] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-200] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-210] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-42] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-58] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-182] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [84-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-124] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-87] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-164] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-193] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>