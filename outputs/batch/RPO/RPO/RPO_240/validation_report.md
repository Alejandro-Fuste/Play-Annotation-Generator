# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_240`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_240/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [72-116] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-184] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-197] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-206] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [73-132] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [73-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-191] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-131] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-276] for track '24' has 1 frames without a visible bounding box.
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