# Play-Annotation-Generator Annotation Review — Slants0to10_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_81`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 18 | START | 18 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 21 | START | 21 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 21 | START | 21 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 21 | START | 21 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 21 | START | 33 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `9` | 21 | START | 21 | 68 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 32 | END | 18 | 32 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `1` | `1` | 37 | START | 37 | 110 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 79 | START | 79 | 89 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 129 | START | 129 | 210 |

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
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 32 | 15 | inferred_complete_timeline |
| `Action_None` | 33 | 78 | 46 | inferred_complete_timeline |
| `Action_ThrowPass` | 79 | 89 | 11 | inferred_complete_timeline |
| `Action_None` | 90 | 116 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 37 | 110 | 74 | inferred_complete_timeline |
| `Action_None` | 111 | 128 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 74 | 57 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_None` | 72 | 95 | 24 | inferred_complete_timeline |
| `Action_None` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_None` | 108 | 114 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 68 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 90 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 116 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 154 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 70 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 133 | 62 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 138 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 32 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 86 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 106 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 160 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 162 | 210 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 68 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 116 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 68 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 86 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 116 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 146 | 174 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 70 | 53 | inferred_complete_timeline |
| `Action_None` | 72 | 106 | 35 | inferred_complete_timeline |
| `Action_None` | 108 | 132 | 25 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 68 | 51 | inferred_complete_timeline |
| `Action_None` | 72 | 74 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 95 | 78 | inferred_complete_timeline |
| `Action_None` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_None` | 109 | 116 | 8 | inferred_complete_timeline |
| `Action_None` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_None` | 142 | 210 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 48 | 31 | inferred_complete_timeline |
| `Action_None` | 50 | 62 | 13 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 138 | 36 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 65 | 48 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 76 | 59 | inferred_complete_timeline |
| `Action_None` | 78 | 82 | 5 | inferred_complete_timeline |
| `Action_None` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 195 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–36 | 34 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 40–43 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 98–104 | 4 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 158–210 | 53 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 195–210 | 16 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 200–203 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [18–32], lower_priority='Action_PassBlock' annotated_start=21, effective_Action_PassBlock_start=33.
- ⚠️ Action 'Action_None' range [18-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [129-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-95] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-62] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-70] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-105] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-68] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-116] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [120-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [146-174] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-68] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-62] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-138] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-90] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-116] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-154] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-70] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-106] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-132] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-116] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [120-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-70] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-133] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-138] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [153-210] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-86] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [162-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-31] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '31' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>