# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_370`
- **Input XML**: `outputs/batch/Power/Power/Power_370/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [11-179] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-117] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-182] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-205] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-248] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-264] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-133] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-116] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-272] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-290] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-109] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-221] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [90-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-137] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-202] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [90-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-248] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-261] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-225] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-236] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-270] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-243] for track '26' has 1 frames without a visible bounding box.
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
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.