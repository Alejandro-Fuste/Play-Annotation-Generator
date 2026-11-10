# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_52`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_None' range [127-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-350] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-312] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-323] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-339] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-324] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-348] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-357] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-303] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-236] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-349] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-229] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-339] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-330] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-287] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-340] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-311] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-342] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-267] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-334] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '25' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.