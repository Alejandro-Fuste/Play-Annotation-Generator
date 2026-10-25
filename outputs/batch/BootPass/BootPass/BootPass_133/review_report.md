# Play-Annotation-Generator Annotation Review — BootPass_133

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_133`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 163
- **Validation Warnings:** 177
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 135
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `21` | `21` |
| ⚠️ END CHANGED | `Action_SnapReceive` | TE | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | TE | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunFlatRoute` | DT1 | defense | `15` | `15` |
| ⚠️ START CHANGED | `Action_BootAway` | CB1 | defense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | CB1 | defense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | DT1 | defense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 1 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `16` | `16` | 2 | START | 2 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `10` | `10` | 50 | START | 50 | 55 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | `16` | `16` | 50 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `19` | `19` | 50 | START | 103 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `20` | `20` | 50 | START | 66 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `21` | `21` | 50 | START | 51 | 52 |
| ⚠️ END CHANGED | `Action_SnapReceive` | TE | `14` | `14` | 56 | END | 2 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | TE | `14` | `14` | 67 | START | 76 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunFlatRoute` | DT1 | `15` | `15` | 91 | START | 91 | 100 |
| ⚠️ START CHANGED | `Action_BootAway` | CB1 | `12` | `12` | 94 | START | 96 | 109 |
| ✅ EXACT | `Action_ThrowPass` | CB1 | `12` | `12` | 111 | START | 111 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | DT1 | `15` | `15` | 113 | START | 113 | 117 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 36 | 35 | inferred_complete_timeline |
| `Action_None` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_None` | 58 | 210 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 47 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 67 | 66 | inferred_complete_timeline |
| `Action_None` | 69 | 76 | 8 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 36 | 35 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 35 | 34 | inferred_complete_timeline |
| `Action_FakeHandoff` | 76 | 81 | 6 | inferred_complete_timeline |
| `Action_FakeHandoff` | 85 | 91 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 22 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 30 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 70 | 197 | 128 | inferred_complete_timeline |
| `Action_RunBlock` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 72 | 210 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 14 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 32 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 53 | 56 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 25 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 103 | 111 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 137 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 139 | 167 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 40 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 59 | 85 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_None` | 119 | 128 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 12 | 11 | inferred_complete_timeline |
| `Action_None` | 15 | 32 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 33 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 86 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 91 | 100 | 10 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 102 | 112 | 11 | inferred_complete_timeline |
| `Action_SecureCatch` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_SecureCatch` | 129 | 144 | 16 | inferred_complete_timeline |
| `Action_None` | 145 | 191 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 13 | 12 | inferred_complete_timeline |
| `Action_None` | 19 | 33 | 15 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 62 | 61 | inferred_complete_timeline |
| `Action_None` | 64 | 137 | 74 | inferred_complete_timeline |
| `Action_None` | 139 | 144 | 6 | inferred_complete_timeline |
| `Action_None` | 153 | 162 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 35 | 34 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 97 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 78 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_BootAway` | 96 | 109 | 14 | inferred_complete_timeline |
| `Action_None` | 110 | 110 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 111 | 120 | 10 | inferred_complete_timeline |
| `Action_None` | 121 | 206 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 95 | 94 | inferred_complete_timeline |
| `Action_None` | 98 | 104 | 7 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 163 | 50 | inferred_complete_timeline |
| `Action_None` | 176 | 187 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 41 | 40 | inferred_complete_timeline |
| `Action_None` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_None` | 64 | 137 | 74 | inferred_complete_timeline |
| `Action_None` | 139 | 146 | 8 | inferred_complete_timeline |
| `Action_None` | 152 | 183 | 32 | inferred_complete_timeline |
| `Action_None` | 185 | 201 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 63 | 62 | inferred_complete_timeline |
| `Action_None` | 65 | 78 | 14 | inferred_complete_timeline |
| `Action_None` | 82 | 167 | 86 | inferred_complete_timeline |
| `Action_None` | 169 | 176 | 8 | inferred_complete_timeline |
| `Action_None` | 180 | 191 | 12 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 209 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

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

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 48–210 | 140 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 60–189 | 124 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 76–209 | 72 | 8 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 77–79 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 78–210 | 104 | 6 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 82–210 | 123 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 100–210 | 82 | 6 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 103–210 | 99 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 103–128 | 21 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 129–185 | 51 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 131–210 | 77 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 143–210 | 68 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 162–210 | 38 | 3 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 180–187 | 8 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 194–210 | 13 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunFlatRoute` and target `15` (2 segments found)
- ⚠️ `Action_BootAway` for actor_track_id `12` (CB1): Annotated start 94 != Inferred start 96
- ⚠️ Ambiguous match for action `Action_SecureCatch` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 143 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [2–56], lower_priority='Action_RunBlock' annotated_start=50, effective_Action_RunBlock_start=57.
- ⚠️ Action 'Action_None' range [2-36] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-63] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-78] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-36] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-56] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-41] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-201] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-62] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-137] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-162] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-35] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-97] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-163] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-47] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-40] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [59-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-12] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-78] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-85] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [96-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [111-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-32] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [2-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [76-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [85-91] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-33] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-67] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [91-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [102-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [113-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-191] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [2-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [19-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [26-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [34-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [53-56] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-13] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-25] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [103-111] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [122-137] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [139-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-30] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [66-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [70-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [200-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [64-68] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [72-210] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-84] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-110] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-174] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-113] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-85] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-101] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-201] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-123] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-111] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-177] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-182] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-174] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '37' has 1 frames without a visible bounding box.
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

</details>