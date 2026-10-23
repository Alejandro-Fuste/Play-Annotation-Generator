# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_1`
- **Input XML**: `output_showcase_final/Sack/Sack_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 4: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-207] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-14] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [186-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-172] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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