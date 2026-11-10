# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_6`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 37 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [7-243] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-46] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-255] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-329] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [275-293] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-253] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-266] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-329] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-282] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-287] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-192] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-294] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-313] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-212] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-226] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-322] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-270] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-329] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-323] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-329] for track '23' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.