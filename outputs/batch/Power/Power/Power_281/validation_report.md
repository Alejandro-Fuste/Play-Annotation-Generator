# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_281`
- **Input XML**: `outputs/batch/Power/Power/Power_281/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-311] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-315] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-333] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-350] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-343] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-270] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-275] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-357] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-262] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-334] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-339] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-344] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-349] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-349] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-359] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-220] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-254] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-338] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-348] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-314] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-338] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-354] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.