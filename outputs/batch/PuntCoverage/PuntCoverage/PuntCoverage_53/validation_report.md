# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_53`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-241] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-255] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-259] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-288] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-296] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-255] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [241-278] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-287] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-20] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-28] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-178] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-148] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-247] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-266] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-299] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [185-248] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-280] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-286] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.