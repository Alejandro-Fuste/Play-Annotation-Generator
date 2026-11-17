# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_81`
- **Input XML**: `outputs/batch/Power/Power/Power_81/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 164: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [18-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-133] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-143] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-209] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-174] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-181] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-198] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-195] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '25' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.