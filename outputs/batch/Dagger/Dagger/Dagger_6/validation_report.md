# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_6`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 448 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 448 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [70–76], lower_priority='Action_PassBlock' annotated_start=73, effective_Action_PassBlock_start=77.
> - Action 'Action_None' range [70-383] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-420] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-435] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-443] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-365] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-432] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-271] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-286] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-418] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-448] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-203] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [70-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-376] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-448] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-375] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-387] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-169] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-284] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [162-165] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [169-267] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-190] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [193-363] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-22] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-288] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-390] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-286] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-357] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-319] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-364] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-369] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-378] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-405] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.