# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_265`
- **Input XML**: `outputs/batch/Power/Power/Power_265/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 530: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 530: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [21-166] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [128-163] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-199] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-186] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-193] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-186] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-204] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [128-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-176] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-161] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-231] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-231] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-260] for track '27' has 2 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.