# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_116`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_116/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_None' range [53-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-174] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-92] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-132] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-133] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 140, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [140-154] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-99] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 53, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [53-53] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-168] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-117] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-64] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-103] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-131] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-170] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-142] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-183] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-274] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-295] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-360] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-187] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-308] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-356] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-361] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [328-330] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '31' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.