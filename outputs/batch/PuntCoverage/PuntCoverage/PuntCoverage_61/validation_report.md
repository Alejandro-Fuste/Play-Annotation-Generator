# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_61`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_Tackle' for track '18' has invalid range: start=210, end=208. Clamping end to start.
> - Action 'Action_PreSnap' range [0-121] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-117] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-218] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-248] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-192] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-199] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-52] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-117] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [185-245] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [249-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-196] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-221] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-243] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-250] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-248] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-264] for track '36' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.