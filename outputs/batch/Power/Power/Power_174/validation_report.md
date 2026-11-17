# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_174`
- **Input XML**: `outputs/batch/Power/Power/Power_174/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 37 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [22-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-184] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-192] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-140] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-243] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-159] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-187] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-195] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-208] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-268] for track '24' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.