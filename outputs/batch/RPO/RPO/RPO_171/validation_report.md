# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_171`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_171/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '16' has invalid range: start=72, end=71. Clamping end to start.
> - Action 'Action_None' range [71-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-155] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-234] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [71-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-82] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-182] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-229] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-236] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-234] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-171] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-76] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 71, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [71-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-218] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [80-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [146-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-113] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-212] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-77] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-228] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-202] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-211] for track '26' has 1 frames without a visible bounding box.
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